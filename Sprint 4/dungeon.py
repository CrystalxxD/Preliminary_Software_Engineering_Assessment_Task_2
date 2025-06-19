import random
import pygame
from pygame.locals import *
from room import Room
from enemy import Boss
from windows import *

class Dungeon:
    def __init__(self, width, height, floors=20, stories=None):
        # Initialize dungeon properties
        self.floors = []  # List to store all dungeon floors
        self.exit_floor_index = floors - 1  # Exit is always on the last floor
        self.exit_room_position = None  # Position of the exit room
        self.stair_positions = {}  # Tracks positions of stairs between floors
        self.key_floor_index = None  # Which floor contains the key
        self.key_room_position = None  # Which room contains the key
        self.room_stories = stories or ["A mysterious room."]  # Room descriptions

        # Generate each floor of the dungeon
        for floor_num in range(floors):
            floor, room_list = self.generate_floor(width, height, floor_num)
            self.floors.append(floor)

        # Place the exit portal in a suitable room
        exit_room_list = [pos for pos, room in self.floors[self.exit_floor_index].items()
                        if abs(pos[0]) + abs(pos[1]) >= 15 and not room.has_enemy]
        
        # Fallback if no distant rooms are available
        if not exit_room_list:
            exit_room_list = list(self.floors[self.exit_floor_index].keys())
        
        if exit_room_list:
            self.exit_room_position = random.choice(exit_room_list)
            exit_room = self.floors[self.exit_floor_index][self.exit_room_position]
            exit_room.is_exit = True  # Mark as exit room
            exit_room.has_enemy = False  # Ensure exit isn't blocked
            exit_room.enemy = None
            exit_room.items = []
            exit_room.story = "A glowing cyan portal shimmers before you. This is the way out."

        # Place the key in a random room
        self.place_key()

    def place_key(self):
        # Find all eligible rooms for placing the key
        eligible_rooms = []
        for f_index, floor in enumerate(self.floors):
            for pos, room in floor.items():
                # Key can't be in rooms with enemies, stairs, or the exit
                if not room.has_enemy and not room.is_stairs and not room.is_exit:
                    eligible_rooms.append((f_index, pos))
        
        # Place the key if eligible rooms exist
        if eligible_rooms:
            self.key_floor_index, self.key_room_position = random.choice(eligible_rooms)
            self.floors[self.key_floor_index][self.key_room_position].set_key()

    def generate_floor(self, width, height, floor_num):
        # Initialize floor and room tracking
        floor = {}
        room_list = []
        x, y = 0, 0  # Start generation from center

        # Generate rooms until we reach our target count
        while len(room_list) < 300:
            pos = (x, y)
            if pos not in floor:
                room = Room(self.room_stories)
                # Starting room (0,0) never has enemies
                if pos == (0, 0):
                    room.has_enemy = False
                    room.enemy = None
                room.is_stairs = False
                room.is_ascend = False
                room.is_descend = False
                floor[pos] = room
                room_list.append(pos)

            # Weighted random movement for organic dungeon layout
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            # Early rooms prefer straight paths, later ones branch more
            weights = [0.3, 0.3, 0.2, 0.2] if len(room_list) < 50 else [0.25] * 4
            dx, dy = random.choices(directions, weights=weights)[0]
            x += dx
            y += dy

        # Find rooms far from center for special placement
        far_rooms = [pos for pos in room_list if abs(pos[0]) + abs(pos[1]) >= 20]
        if not far_rooms:
            far_rooms = [pos for pos in room_list if pos != (0, 0)]
        
        # Place descending stairs (except on first floor)
        if floor_num > 0 and far_rooms:
            stair_room = random.choice(far_rooms)
            floor[stair_room].is_stairs = True
            floor[stair_room].is_descend = True
            
            # Every even floor has a boss guarding the stairs
            if floor_num % 2 == 0:
                floor[stair_room].has_enemy = True
                floor[stair_room].enemy = Boss(floor_num)
                floor[stair_room].items = []

        # Place ascending stairs (except on last floor)
        if floor_num < self.exit_floor_index and far_rooms:
            stair_room = random.choice(far_rooms)
            floor[stair_room].is_stairs = True
            floor[stair_room].is_ascend = True

        return floor, room_list

    def get_room(self, floor_num, position):
        # Safely get a room reference
        if floor_num < 0 or floor_num >= len(self.floors):
            return None
        return self.floors[floor_num].get(position)

    def room_exists(self, floor_num, position):
        # Check if a room exists at given coordinates
        if floor_num < 0 or floor_num >= len(self.floors):
            return False
        return position in self.floors[floor_num]

    def draw_pygame_minimap(self, surface, floor_num, player_pos, x, y, width, height):
        # Draw a minimap representation of the current floor
        if floor_num < 0 or floor_num >= len(self.floors):
            return
            
        floor = self.floors[floor_num]
        if not floor:
            return
        
        positions = list(floor.keys())
        if not positions:
            return
        
        # Calculate bounds for proper scaling
        min_x = min(pos[0] for pos in positions)
        max_x = max(pos[0] for pos in positions)
        min_y = min(pos[1] for pos in positions)
        max_y = max(pos[1] for pos in positions)
        
        range_x = max_x - min_x + 1
        range_y = max_y - min_y + 1
        
        # Calculate cell size to fit minimap in given dimensions
        cell_size = min(width // range_x, height // range_y)
        offset_x = (width - (range_x * cell_size)) // 2
        offset_y = (height - (range_y * cell_size)) // 2
        
        # Draw each room with appropriate coloring
        for pos in positions:
            room = floor[pos]
            px = x + offset_x + (pos[0] - min_x) * cell_size
            py = y + offset_y + (max_y - pos[1]) * cell_size
            
            # Determine room color based on its properties
            if pos == player_pos:
                colour = BLUE  # Player's current position
            elif self.exit_floor_index == floor_num and pos == self.exit_room_position:
                colour = GREEN  # Exit portal
            elif self.key_floor_index == floor_num and pos == self.key_room_position and room.has_key:
                colour = YELLOW  # Key location
            elif room.is_ascend:
                colour = (0, 255, 0)  # Ascending stairs
            elif room.is_descend and room.has_enemy and isinstance(room.enemy, Boss):
                colour = PURPLE  # Boss room
            elif room.is_descend:
                colour = (255, 0, 0)  # Descending stairs
            elif room.has_enemy:
                colour = (255, 0, 0)  # Regular enemy
            else:
                colour = (100, 100, 100)  # Empty room
            
            # Draw the room rectangle
            pygame.draw.rect(surface, colour, (px, py, cell_size, cell_size))
            pygame.draw.rect(surface, BLACK, (px, py, cell_size, cell_size), 1)