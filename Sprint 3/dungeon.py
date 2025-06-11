import random
from room import Room
from enemy import Boss

class Dungeon:
    def __init__(self, width, height, floors=20):
        self.floors = []
        self.exit_floor_index = floors - 1
        self.exit_room_position = None
        self.stair_positions = {}
        self.key_floor_index = None
        self.key_room_position = None

        for floor_num in range(floors):
            floor, room_list = self.generate_floor(width, height, floor_num)
            self.floors.append(floor)

        # Set exit on final floor
        exit_room_list = list(self.floors[self.exit_floor_index].keys())
        if len(exit_room_list) >= 20:
            self.exit_room_position = exit_room_list[19]
            self.floors[self.exit_floor_index][self.exit_room_position].is_exit = True

        # Place key in furthest room from (0,0)
        max_dist = -1
        for f_index, floor in enumerate(self.floors):
            for pos in floor:
                dist = abs(pos[0]) + abs(pos[1])
                if dist > max_dist:
                    max_dist = dist
                    self.key_floor_index = f_index
                    self.key_room_position = pos
        self.floors[self.key_floor_index][self.key_room_position].set_key()

    def generate_floor(self, width, height, floor_num):
        floor = {}
        room_list = []
        x, y = 0, 0

        while len(room_list) < 300:
            pos = (x, y)
            if pos not in floor:
                room = Room()
                if pos == (0, 0):
                    room.has_enemy = False
                    room.enemy = None
                room.is_stairs = False
                floor[pos] = room
                room_list.append(pos)

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            weights = [0.3, 0.3, 0.2, 0.2] if len(room_list) < 50 else [0.25] * 4
            dx, dy = random.choices(directions, weights=weights)[0]
            x += dx
            y += dy

        # Skip stairs on exit floor
        if floor_num != self.exit_floor_index:
            far_rooms = [pos for pos in room_list if abs(pos[0]) + abs(pos[1]) >= 80 and pos != (0, 0)]
            stair_room = random.choice(far_rooms if far_rooms else room_list)
            for pos in floor:
                floor[pos].is_stairs = False
            floor[stair_room].is_stairs = True
            floor[stair_room].has_enemy = False
            floor[stair_room].enemy = None
            self.stair_positions[floor_num] = stair_room

            # Optional: boss guards stairs
            if floor_num % 2 == 0:
                floor[stair_room].has_enemy = True
                floor[stair_room].enemy = Boss(floor_num)

        return floor, room_list

    def get_room(self, floor_num, position):
        return self.floors[floor_num].get(position)

    def room_exists(self, floor_num, position):
        return position in self.floors[floor_num]

    def draw_minimap(self, floor_num, player_pos):
        floor = self.floors[floor_num]
        min_x = min(pos[0] for pos in floor)
        max_x = max(pos[0] for pos in floor)
        min_y = min(pos[1] for pos in floor)
        max_y = max(pos[1] for pos in floor)
        print("Minimap:")
        for y in range(max_y, min_y - 1, -1):
            line = ""
            for x in range(min_x, max_x + 1):
                pos = (x, y)
                if pos == player_pos:
                    line += "P "
                elif floor_num == self.exit_floor_index and pos == self.exit_room_position:
                    line += "X "
                elif floor_num == self.key_floor_index and pos == self.key_room_position:
                    line += "K "
                elif pos in floor:
                    room = floor[pos]
                    if room.is_stairs and room.has_enemy and room.enemy and room.enemy.hp > 0:
                        line += "B "
                    elif room.is_stairs:
                        line += "S "
                    elif room.has_enemy and room.enemy and room.enemy.hp > 0:
                        line += "E "
                    else:
                        line += ". "
                else:
                    line += "  "
            print(line)