import random
import pygame
from pygame.locals import *
from room import Room
from enemy import Boss
from windows import *

class Dungeon:
    def __init__(self, width, height, floors=30, stories=None):
        self.floors = []
        self.exit_floor_index = floors - 1
        self.exit_room_position = None
        self.stair_positions = {}
        self.key_floor_index = None
        self.key_room_position = None
        self.room_stories = stories or ["A mysterious room."]

        for floor_num in range(floors):
            floor, room_list = self.generate_floor(width, height, floor_num)
            self.floors.append(floor)

        # Set exit on final floor
        exit_room_list = list(self.floors[self.exit_floor_index].keys())
        if exit_room_list:
            self.exit_room_position = exit_room_list[-1]
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
        if self.key_floor_index is not None and self.key_room_position is not None:
            self.floors[self.key_floor_index][self.key_room_position].set_key()

    def generate_floor(self, width, height, floor_num):
        floor = {}
        room_list = []
        x, y = 0, 0

        while len(room_list) < 300:
            pos = (x, y)
            if pos not in floor:
                room = Room(self.room_stories)
                if pos == (0, 0):  # Starting room
                    room.has_enemy = False
                    room.enemy = None
                room.is_stairs = False
                room.is_ascend = False
                room.is_descend = False
                floor[pos] = room
                room_list.append(pos)

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            weights = [0.3, 0.3, 0.2, 0.2] if len(room_list) < 50 else [0.25] * 4
            dx, dy = random.choices(directions, weights=weights)[0]
            x += dx
            y += dy

        # Get rooms far from start
        far_rooms = [pos for pos in room_list if abs(pos[0]) + abs(pos[1]) >= 20]
        if not far_rooms:
            far_rooms = [pos for pos in room_list if pos != (0, 0)]
        
        # Place descending stairs on all floors except bottom floor (0)
        if floor_num > 0 and far_rooms:
            stair_room = random.choice(far_rooms)
            floor[stair_room].is_stairs = True
            floor[stair_room].is_descend = True
            
            # Place boss on descending stairs every even floor (0, 2, 4...)
            if floor_num % 2 == 0:
                floor[stair_room].has_enemy = True
                floor[stair_room].enemy = Boss(floor_num)
                floor[stair_room].items = []  # Clear items from boss room

        # Place ascending stairs on all floors except top floor
        if floor_num < self.exit_floor_index and far_rooms:
            available_rooms = [pos for pos in far_rooms if pos != self.stair_positions.get(floor_num, None)]
            if not available_rooms:
                available_rooms = far_rooms
                
            stair_room = random.choice(available_rooms)
            floor[stair_room].is_stairs = True
            floor[stair_room].is_ascend = True

            # Place boss on ascending stairs every even floor (0, 2, 4...)
            if floor_num % 2 == 0:
                floor[stair_room].has_enemy = True
                floor[stair_room].enemy = Boss(floor_num)
                floor[stair_room].items = []  # Clear items from boss room

        return floor, room_list

    def get_room(self, floor_num, position):
        if floor_num < 0 or floor_num >= len(self.floors):
            return None
        return self.floors[floor_num].get(position)

    def room_exists(self, floor_num, position):
        if floor_num < 0 or floor_num >= len(self.floors):
            return False
        return position in self.floors[floor_num]

    def draw_pygame_minimap(self, surface, floor_num, player_pos, x, y, width, height):
        if floor_num < 0 or floor_num >= len(self.floors):
            return
            
        floor = self.floors[floor_num]
        if not floor:
            return
        
        positions = list(floor.keys())
        if not positions:
            return
        
        min_x = min(pos[0] for pos in positions)
        max_x = max(pos[0] for pos in positions)
        min_y = min(pos[1] for pos in positions)
        max_y = max(pos[1] for pos in positions)
        
        range_x = max_x - min_x + 1
        range_y = max_y - min_y + 1
        
        cell_size = min(width // range_x, height // range_y)
        offset_x = (width - (range_x * cell_size)) // 2
        offset_y = (height - (range_y * cell_size)) // 2
        
        for pos in positions:
            room = floor[pos]
            px = x + offset_x + (pos[0] - min_x) * cell_size
            py = y + offset_y + (max_y - pos[1]) * cell_size  # Invert y-axis
            
            # Determine cell colour
            if pos == player_pos:
                colour = BLUE  # Player
            elif self.exit_floor_index == floor_num and pos == self.exit_room_position:
                colour = GREEN  # Exit
            elif self.key_floor_index == floor_num and pos == self.key_room_position and floor[pos].has_key:
                colour = YELLOW  # Key
            elif room.is_ascend:
                colour = (0, 255, 0)  # Green for ascend stairs
            elif room.is_descend and room.has_enemy and isinstance(room.enemy, Boss):
                colour = PURPLE  # Purple for boss rooms
            elif room.is_descend:
                colour = (255, 0, 0)  # Red for descend stairs
            elif room.has_enemy:
                colour = (255, 0, 0)  # Red for regular enemies
            else:
                colour = (100, 100, 100)  # Gray for empty rooms
            
            pygame.draw.rect(surface, colour, (px, py, cell_size, cell_size))
            pygame.draw.rect(surface, BLACK, (px, py, cell_size, cell_size), 1)