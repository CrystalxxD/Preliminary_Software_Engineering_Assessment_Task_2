import random
from room import Room

class Dungeon:
    def __init__(self, width, height, floors=2):
        self.floors = []
        self.exit_room_position = None
        self.stairs_position = None  # Room that leads to next floor
        for floor_num in range(floors):
            self.floors.append(self.generate_floor(width, height, floor_num))

    def generate_floor(self, width, height, floor_num):
        floor = {}
        room_list = []
        x, y = 0, 0
        for _ in range(100):  # 20 rooms
            floor[(x, y)] = Room()
            room_list.append((x, y))
            dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
            x += dx
            y += dy

        # Place key in farthest room on floor 0
        if floor_num == 0 and room_list:
            farthest = max(room_list, key=lambda pos: abs(pos[0]) + abs(pos[1]))
            floor[farthest].has_key = True
            floor[farthest].has_enemy = False
            # Place stairs in second farthest
            room_list.remove(farthest)
            if room_list:
                stairs_pos = max(room_list, key=lambda pos: abs(pos[0]) + abs(pos[1]))
                floor[stairs_pos].is_stairs = True
                self.stairs_position = stairs_pos

        # Place exit in farthest room on floor 1
        if floor_num == 1 and room_list:
            farthest = max(room_list, key=lambda pos: abs(pos[0]) + abs(pos[1]))
            floor[farthest].is_exit = True
            self.exit_room_position = farthest

        return floor

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
                elif floor_num == 0 and pos == self.stairs_position:
                    line += "S "
                elif floor_num == 1 and pos == self.exit_room_position:
                    line += "X "
                elif pos in floor:
                    room = floor[pos]
                    if room.has_enemy and room.enemy and room.enemy.hp > 0:
                        line += "E "
                    elif room.has_key:
                        line += "K "
                    else:
                        line += ". "
                else:
                    line += "  "
            print(line)
