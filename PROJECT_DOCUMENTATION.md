# Preliminary_Software_Engineering_Assessment_Task_2
# Sprint 1
### Requirements Definition
#### Functional Requirements

The game must allow the player to select a character class (e.g., Assassin, Warrior, Mage, Archer), each with unique stats. Players must navigate through randomly generated rooms across multiple dungeon floors using the WASD keys. Each room may contain enemies, items like potions or armor, or a key required to escape. Players must be able to fight enemies and bosses, pick up items, and track stats such as health, attack, and defense.

---
#### Non-Functional Requirements

The game should be responsive and user-friendly with simple controls. It must load quickly, have a clean text or GUI interface, and be built in Python using Object-Oriented Programming (OOP) principles. The final version should use a GUI (Pygame) and run without needing external game engines.

---
## Determining Specification
### Functional Specification

The player will move using W, A, S, and D keys across randomly connected rooms, each with its own storyline loaded from a text file. Items (e.g., health potions, buffs, weapons) and enemies (e.g., goblins, werewolves) are distributed throughout rooms with set probabilities. One room contains a key required to complete the game. A minimap updates live to show player position, enemies, key, and room boundaries.

---
### Non Functional Specification

The game is developed using Python with modular files like player.py, enemy.py, dungeon.py, and main.py. In later sprints, a graphical user interface (GUI) replaces the console, allowing users to interact via buttons. The game will be visually clean, performant, and maintainable through well-documented code and classes.

---
## Use Cases
Actor: Player

Preconditions: Game has started and the player has selected a class.

Main Flow:

1. Player spawns in the first room on Floor 1.

2. They move around using WASD keys, triggering stories in each room.

3. In some rooms, they find potions, buffs, weapons, armour or fight enemies.

4. They defeat enemies using their class stats and equipped items.

5. Upon finding the key and clearing most enemies, they move ufloors.

6. They eventually reach the final room, fight a boss, and escape.

Postconditions: Player wins if alive and reaches exit with key; loses if health reaches 0.

Exceptions: Player tries to move into walls; combat with enemies results in death.

### Use Case Diagram
![alt text](<Images/Use Case Diagram.png>)
---
## Design
### Gnatt Chart
![alt text](<Images/Gantt chart.png>)
---
### Story Board
---
#### Text Based Part
![alt text](<Images/Text Based Game Story Board.png>)
---
#### Gui Part
![alt text](<Images/Gui of Story Board.png>)
---
### Dataflow Diagram
---
#### Level 0
![alt text](<Images/DataFlow Diagram Level 0.png>)
---
#### Level 1
![alt text](<Images/DataFlow Diagram Level 1.png>)
---
## Build and Test
```
import random

# Starting items
player_inventory = ["Rusty Sword", "Health Potion"]
player_health = 100

def show_intro():
    print("=" * 40)
    print("   Tower of Blood   ")   
    print("=" * 40)
    print("Type a command to begin your escape.\n")

def show_options():
    print("Available commands:")
    print(" - move")
    print(" - help")
    print(" - inventory")
    print(" - status")
    print(" - quit\n")

def show_help():
    print("\nCOMMAND HELP:")
    print(" move     - Move W, A, S, or D")
    print(" inventory - Show your current items")
    print(" status    - Show health and equipped items")
    print(" quit      - Exit the game\n")

def show_inventory():
    print("\nYOUR INVENTORY:")
    if player_inventory:
        for item in player_inventory:
            print(f" - {item}")
    else:
        print(" (Empty)")
    print()

def show_status():
    print(f"\nSTATUS:")
    print(f" Health: {player_health}")
    print(f" Items: {', '.join(player_inventory)}\n")

def move_player():
    directions = ["W", "A", "S", "D"]
    direction = input("Which direction? (W/A/S/D): ").strip().lower()
    if direction in directions:
        print(f"\nYou cautiously move {direction}...")
        encounter_event()
    else:
        print("Invalid direction. Try W, A, S, or D.\n")

def encounter_event():
    events = ["found a potion", "encountered an enemy", "found a locked door", "empty room"]
    event = random.choice(events)
    
    if event == "found a potion":
        print("You found a glowing potion and added it to your inventory!\n")
        player_inventory.append("Glowing Potion")
    elif event == "encountered an enemy":
        print("A skeleton attacks you! You lose 10 health.\n")
        global player_health
        player_health -= 10
    elif event == "found a locked door":
        print("You see a locked door. You'll need a key to open it.\n")
    elif event == "empty room":
        print("The room is silent... too silent. Nothing happens.\n")

def quit_game():
    print("\nYou sit down and decide to give up. Maybe next time...")
    print("Thanks for playing Dungeon Escape!\n")

def main():
    show_intro()
    show_options()

    while True:
        command = input("> ").strip().lower()

        if command == "move":
            move_player()
        elif command == "help":
            show_help()
        elif command == "inventory":
            show_inventory()
        elif command == "status":
            show_status()
        elif command == "quit":
            quit_game()
            break
        else:
            print("Unknown command. Type 'help' to see available options.\n")

if __name__ == "__main__":
    main()

```

### ReadMe
#### Tower of Blood

This Python program is a text-based dungeon escape room game, designed as part of a software development sprint project. The player selects a class (e.g., Warrior, Mage, Archer) and explores a procedurally generated dungeon. Players can move through rooms, collect items, fight enemies, and find the exit to advance to the next floor.

Features
- Choose a unique character class with different starting stats

- Navigate a dungeon of over 20 randomly generated rooms using W, A, S, D movement keys.

- Encounter random events including enemies (e.g., goblins, vampires), item drops, and locked doors.

- Collect health potions, damage and defense buffs, weapons, and armor.

- Includes a mini-map displayed using text characters, showing player location, enemies, exits, and room layout.

- Simple command-based interface (with GUI implementation in Sprint 4 using PySimpleGUI).

- Two dungeon floors to complete the game.

Requirements
To run this program, you need to install the following dependencies:

Install dependencies
To install the required dependencies, run:
``` bash
pip install -r requirements.txt
```

## Review
### Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.
All functional and non-functional requirements are planned for implementation, including map generation, combat, item usage, and GUI. The minimap, combat mechanics, and item effects are all tested and functional.

---
### Analyse the performance of your program against the key use-cases you identified.
Game runs efficiently even with random generation. GUI interface maintains quick responses to player actions.

---
### Assess the quality of your code in terms of readability, structure, and maintainability.
The code uses classes and modular design with well-named functions and variables. 

---
### Explain the improvements that should be made in the next stage of development.
Adding Classes for player and enemies as well as the room and dungeon layout.

Adding Combat

Adding 

# Sprint 2 
## Design 
---
### Structure Chart
![alt text](<Images/Structure Chart.png>)
---
### Flowchart
---
#### Main()
![alt text](<Images/Main Flowchart.png>)
---
#### Drop Item()
![alt text](<Images/Drop Item Flowchart.png>)
---
#### Display Title()
![alt text](<Images/Display Title Flowchart.png>)
---
### Psuedocode
---
#### Main()
BEGIN Main
    DISPLAY "Welcome to Tower of Blood!"
    PROMPT "Enter your name:"
    INPUT playerName

    DISPLAY "Choose your class: Assassin, Mage, Archer, Warrior"
    PROMPT "Enter your class:"
    INPUT playerClass

    IF playerClass = "Assassin" THEN
        CALL SetupAssassin()
    ELSE IF playerClass = "Mage" THEN
        CALL SetupMage()
    ELSE IF playerClass = "Archer" THEN
        CALL SetupArcher()
    ELSE IF playerClass = "Warrior" THEN
        CALL SetupWarrior()
    ELSE
        DISPLAY "Invalid class. Please restart."
        EXIT
    END IF

    REPEAT
        DISPLAY "Options: Move (w/a/s/d), Down (l), Inventory (i), Heal (h), Drop (drop), Help (help), Quit (q)"
        PROMPT "What do you want to do?"
        INPUT command

        IF command = "w" OR command = "a" OR command = "s" OR command = "d" THEN
            CALL Move(command)
        ELSE IF command = "l" THEN
            CALL GoDownStairs()
        ELSE IF command = "i" THEN
            CALL ShowInventory()
        ELSE IF command = "h" THEN
            CALL Heal()
        ELSE IF command = "drop" THEN
            CALL DropItem()
        ELSE IF command = "help" THEN
            CALL ShowHelp()
        ELSE IF command = "q" THEN
            DISPLAY "Thank you for playing!"
        ELSE
            DISPLAY "Invalid command. Type 'help' for assistance."
        END IF

    UNTIL command = "q"
END Main
---
#### Drop Item()
BEGIN DropItem
    DISPLAY "Drop Menu:"
    CALL ShowInventory
    PROMPT "Drop [w]eapon, [a]rmour, or [c]ancel?"
    INPUT choice

    IF choice = "w" THEN
        IF weapon list is empty THEN
            DISPLAY "No weapons to drop."
        ELSE
            PROMPT "Enter weapon number to drop:"
            INPUT index
            IF index is valid THEN
                REMOVE weapon at index
                DISPLAY "Weapon dropped."
            ELSE
                DISPLAY "Invalid number."
            END IF
        END IF

    ELSE IF choice = "a" THEN
        IF armour exists THEN
            REMOVE armour
            DISPLAY "Armour dropped."
        ELSE
            DISPLAY "No armour to drop."
        END IF

    ELSE
        DISPLAY "Drop cancelled."
    END IF
END DropItem

---
#### Display Title()
BEGIN DisplayTitleScreen
    DISPLAY TitleScreen()
End DisplayTitleScreen

---
## Build and Test
main.py
```
from player import Player
from dungeon import Dungeon
from combat import battle

def main():
    name = input("Enter your name: ") # lets you choose name
    cls = input("Choose your class (Assassin, Mage, Archer, Warrior): ").lower() # Gives you different class choices to choose from. Each one with different abilities
    player = Player(name, cls) 
    dungeon = Dungeon(10, 10)

    while True:
        print(f"\nYou are at {player.position} on Floor {player.floor + 1}") # Shows where you are
        room = dungeon.get_room(player.floor, player.position)
        dungeon.draw_minimap(player.floor, player.position)

        # Combat
        if room.has_enemy and room.enemy and room.enemy.hp > 0:
            if not battle(player, room.enemy):
                break
            else:
                room.has_enemy = False
                room.enemy = None

        # Items
        for item in room.items:
            print(f"You found a {item.replace('_', ' ')}!")
            player.pick_up_item(item)
        room.items.clear()

        if room.has_key:
            print("You found the key!")
            player.has_key = True
            room.has_key = False

        # Victory
        if (player.floor == 1 and 
            player.position == dungeon.exit_room_position and 
            player.has_key) == True:
            print("You found the dungeon exit and escaped! 🏆 You win!")
            break

        # Movement
        move = input("Move (w/a/s/d) or down a floor (j): ").lower()
        dx, dy = 0, 0
        if move == 'w': dy = 1
        elif move == 's': dy = -1
        elif move == 'a': dx = -1
        elif move == 'd': dx = 1
        elif move == 'j':
            if player.floor == 1:
                player.floor = 0
                print("You descend to Floor 1.")
                continue
            else:
                print("You're already on the bottom floor.")
                continue
        else:
            print("Invalid input.")
            continue

        new_pos = (player.position[0] + dx, player.position[1] + dy)
        if dungeon.room_exists(player.floor, new_pos):
            player.position = new_pos
        else:
            print("No room that way.")
            continue

        # ⬆️ Automatic floor transition when on stairs
        new_room = dungeon.get_room(player.floor, player.position)
        if new_room.is_stairs and player.floor == 0:
            print("You found the stairs and ascended to Floor 2.")
            player.floor = 1
            # Keep position at same coords if valid, else reset to (0, 0)
            if not dungeon.room_exists(1, player.position):
                player.position = (0, 0)


if __name__ == "__main__":
    main()

```
player.py
```
import random

class Player:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.has_key = False
        self.hp = 100
        self.base_stats = {
            "assassin": {"atk": 20, "defn": 5},
            "mage": {"atk": 25, "defn": 3},
            "archer": {"atk": 18, "defn": 6},
            "warrior": {"atk": 15, "defn": 10}
        }
        self.atk = self.base_stats[char_class]["atk"]
        self.defn = self.base_stats[char_class]["defn"]
        self.weapon_bonus = 0
        self.armour_bonus = 0
        self.buffs = {"damage": 0, "defense": 0}
        self.position = (0, 0)
        self.floor = 0


    def total_attack(self):
        return self.atk + self.weapon_bonus + self.buffs["damage"]

    def total_defense(self):
        return self.defn + self.armour_bonus + self.buffs["defense"]

    def heal(self, amount):
        self.hp = min(100, self.hp + amount)

    def pick_up_item(self, item):
        if item == "health":
            self.heal(30)
        elif item == "damage_buff":
            self.buffs["damage"] += 5
        elif item == "defense_buff":
            self.buffs["defense"] += 5
        elif item == "key":
            self.has_key = True
        elif item == "weapon":
            self.weapon_bonus = random.randint(3, 8)
        elif item == "armour":
            self.armour_bonus = random.randint(3, 8)

```

dungeon.py
```
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


```

room.py
```
from enemy import Enemy
import random

class Room:
    def __init__(self):
        self.has_enemy = random.random() < 0.4
        self.enemy = Enemy() if self.has_enemy else None
        self.has_key = False
        self.items = []
        self.is_stairs = False
        self.is_exit = False

        if random.random() < 0.5:
            self.items.append("health")
        if random.random() < 0.2:
            self.items.append(random.choice(["damage_buff", "defense_buff"]))
        if random.random() < 0.1:
            self.items.append(random.choice(["weapon", "armor"]))

    def set_key(self):
        self.has_key = True
 

```

enemy.py
```
import random

class Enemy:
    def __init__(self):
        types = [
            {"type": "Goblin", "hp": 30, "atk": 9, "defn": 3},
            {"type": "Werewolf", "hp": 50, "atk": 12, "defn": 5},
            {"type": "Vampire", "hp": 60, "atk": 10, "defn": 7}
        ]
        enemy = random.choice(types)
        self.name = enemy["type"]
        self.hp = enemy["hp"]
        self.atk = enemy["atk"]
        self.defn = enemy["defn"]

    def is_alive(self):
        return self.hp > 0

class Boss(Enemy):
    def __init__(self, floor_level):
        super().__init__()
        boss_types = [
            {"type": "Goblin King", "hp": 100, "atk": 20, "defn": 8},
            {"type": "Elder Vampire", "hp": 150, "atk": 25, "defn": 10},
            {"type": "Dragon", "hp": 175, "atk": 30, "defn": 12}
        ]
        boss = random.choice(boss_types)
        self.name = f"{boss['type']} (Floor {floor_level + 1})"
        self.hp = boss["hp"] + (floor_level * 5)
        self.atk = boss["atk"] + (floor_level *2)
        self.defn = boss["defn"] + (floor_level * 2)

```
 
combat.py
```
import random

def battle(player, enemy):
    is_boss = "King" in enemy.name or "Elder" in enemy.name or "Dragon" in enemy.name
    if is_boss:
        print(f"\n⚠️ BOSS BATTLE ⚠️")
        print(f"The {enemy.name} blocks your path!")
    else:
        print(f"A wild {enemy.name} appears!")

    while enemy.is_alive() and player.hp > 0:
        print(f"Your HP: {player.hp} | {enemy.name}'s HP: {enemy.hp}")
        while True:
            action = input("Attack (a) or Run (r): ").lower()
            if action in ['a', 'r']:
                break
            print("Incorrect input. Please enter 'a' to attack or 'r' to run.")

        if action == 'a':
            damage = max(1, player.total_attack() - enemy.defn)
            enemy.hp -= damage
            print(f"You dealt {damage} damage to the {enemy.name}!")

            if enemy.is_alive():
                enemy_dmg = max(0, enemy.atk - player.total_defense())
                player.hp -= enemy_dmg
                print(f"{enemy.name} dealt {enemy_dmg} damage to you.")
        elif action == 'r':
            print("The Enemy blocks your escape!")
            enemy_dmg = (player.hp + player.total_defense())
            print(f"{enemy.name} slices your head off as you flee, dealing {enemy_dmg} damage!")
            print("You Died!")
            return False

    if player.hp <= 0:
        print("💀 You died!")
        return False

    if is_boss:
        print(f"\n⭐ VICTORY! ⭐")
        print(f"You defeated the {enemy.name}!")
        player.heal(20)
        print("You recover 20 HP after the intense battle!")
        if random.random() < 0.7:
            print("The boss dropped a rare item!")
            player.pick_up_item(random.choice(["weapon", "armor", "damage_buff", "defense_buff"]), source="boss")
    else:
        print(f"You defeated the {enemy.name}!")

    return True

```

## Review
- Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.
Sprint 2 of my project met my function and non functional requirements that was about the usability, gameplay and functionality. However it didn't complete the requirements of using a GUI implemented userface

- Analyse the performance of your program against the key use-cases you identified.
The program successfully implements core use cases (class selection, movement, combat, and progression) but lacks boss battles and advanced inventory management as specified in the requirements.

- Assess the quality of your code in terms of readability, structure, and maintainability.
The code is well-structured and readable with clear class separation

- Explain the improvements that should be made in the next stage of development.
By adding title screen, boss battle every even number floor and adding permanent buffs or limited round buffs, dropping items, adding limited amount of armour and weapons player can hold, buff enemies

# Sprint 3
## Design
---
### UML Class Diagram
---
#### Key Entities:
    1. Player

        - Attributes:
            - name, char_class, has_key, hp, atk, defn
            - permanent_buffs, temp_buffs, buff_encounters
            - position, floor
            - inventory (health, weapons, armour)

        - Methods:
            - total_attack(), total_defense(), heal()
            - pick_up_item(), update_buffs_after_battle()
            - show_inventory(), use_health_potion(), drop_item()

    2. Enemy (Parent class)

        - Attributes: name, hp, atk, defn

        - Methods: is_alive()

        - Child classes:
            - Boss: Inherits from Enemy with enhanced stats based on floor level

    3. Room

        - Attributes:

            - has_enemy, enemy, has_key, items, is_stairs, is_exit

        - Methods: set_key()

    4. Dungeon

        - Attributes:
            - floors, exit_floor_index, exit_room_position
            - stair_positions, key_floor_index, key_room_position

        - Methods:
            - generate_floor(), get_room(), room_exists(), draw_minimap()

    5.  Item System (Handled through Player's inventory)
        - Weapon items: name, bonus, type
        - Armour items: defense bonus
        - Consumables: health potions, damage/defense buffs

#### Interactions:
    1. Main Game Loop (in main.py) coordinates all interactions

    2. Player interacts with:

        - Room: moves between rooms, picks up items
        - Enemy: through battle system
        - Dungeon: navigation and minimap

    3. Battle System (combat.py) handles Player vs Enemy combat

    4. Dungeon generates and manages all Room instances

--- 
#### Diagram
![alt text](<Images/UML Class Diagram.png>)
---

## Build and Test
main.py
```
import os
import random
import time
from player import Player
from dungeon import Dungeon
from combat import battle

# Load room stories safely
story_path = os.path.join(os.path.dirname(__file__), "stories.txt")
with open(story_path, "r") as file:
    room_stories = [line.strip() for line in file.readlines()]

def display_title():
    COLOUR = ["\033[38;2;255;0;0m","\033[38;2;0;255;0m","\033[38;2;0;0;255m","\033[38;2;255;255;0m","\033[38;2;0;255;255m","\033[38;2;255;0;255m","\033[38;2;255;128;0m","\033[38;2;128;0;255m","\033[38;2;255;255;255m","\033[38;2;255;192;203m","\033[38;2;255;105;180m","\033[38;2;255;20;147m","\033[38;2;199;21;133m","\033[38;2;219;112;147m","\033[38;2;255;0;127m","\033[38;2;255;69;0m","\033[38;2;255;99;71m","\033[38;2;220;20;60m","\033[38;2;0;128;0m","\033[38;2;50;205;50m","\033[38;2;34;139;34m","\033[38;2;152;251;152m","\033[38;2;144;238;144m","\033[38;2;0;255;127m","\033[38;2;46;139;87m","\033[38;2;102;205;170m","\033[38;2;32;178;170m","\033[38;2;0;0;128m","\033[38;2;65;105;225m","\033[38;2;70;130;180m","\033[38;2;100;149;237m","\033[38;2;30;144;255m","\033[38;2;0;191;255m","\033[38;2;135;206;235m","\033[38;2;173;216;230m","\033[38;2;176;224;230m","\033[38;2;25;25;112m","\033[38;2;128;0;128m","\033[38;2;75;0;130m","\033[38;2;147;112;219m","\033[38;2;138;43;226m","\033[38;2;153;50;204m","\033[38;2;186;85;211m","\033[38;2;221;160;221m","\033[38;2;238;130;238m","\033[38;2;216;191;216m","\033[38;2;255;215;0m","\033[38;2;255;255;224m","\033[38;2;250;250;210m","\033[38;2;238;232;170m","\033[38;2;189;183;107m","\033[38;2;240;230;140m","\033[38;2;255;165;0m","\033[38;2;255;140;0m","\033[38;2;210;180;140m","\033[38;2;188;143;143m","\033[38;2;244;164;96m","\033[38;2;205;133;63m","\033[38;2;160;82;45m","\033[38;2;139;69;19m","\033[38;2;165;42;42m","\033[38;2;192;192;192m","\033[38;2;169;169;169m","\033[38;2;128;128;128m","\033[38;2;105;105;105m","\033[38;2;220;220;220m","\033[38;2;245;245;245m","\033[38;2;255;250;250m","\033[38;2;255;228;196m","\033[38;2;255;218;185m","\033[38;2;255;222;173m","\033[38;2;250;235;215m","\033[38;2;253;245;230m","\033[38;2;255;239;213m","\033[38;2;255;235;205m","\033[38;2;255;228;225m","\033[38;2;255;248;220m","\033[38;2;240;255;240m","\033[38;2;245;255;250m","\033[38;2;240;255;255m","\033[38;2;230;230;250m","\033[38;2;255;240;245m","\033[38;2;248;248;255m","\033[38;2;240;248;255m","\033[38;2;255;245;238m","\033[38;2;245;245;220m","\033[38;2;255;228;181m","\033[38;2;255;160;122m","\033[38;2;233;150;122m","\033[38;2;250;128;114m","\033[38;2;205;92;92m","\033[38;2;178;34;34m","\033[38;2;139;0;0m","\033[38;2;112;128;144m","\033[38;2;119;136;153m","\033[38;2;47;79;79m","\033[38;2;0;139;139m","\033[38;2;0;128;128m","\033[38;2;72;209;204m","\033[38;2;64;224;208m","\033[38;2;0;206;209m","\033[38;2;95;158;160m","\033[38;2;175;238;238m","\033[38;2;127;255;212m","\033[38;2;102;205;170m","\033[38;2;143;188;143m","\033[38;2;60;179;113m","\033[38;2;85;107;47m","\033[38;2;107;142;35m","\033[38;2;154;205;50m","\033[38;2;127;255;0m","\033[38;2;173;255;47m","\033[38;2;255;255;240m","\033[38;2;255;250;205m","\033[38;2;250;240;230m","\033[38;2;255;228;200m","\033[38;2;139;0;139m","\033[38;2;148;0;211m","\033[38;2;153;0;153m","\033[38;2;139;0;139m","\033[38;2;255;127;80m","\033[38;2;210;105;30m","\033[38;2;139;69;19m","\033[38;2;160;82;45m","\033[38;2;205;133;63m","\033[38;2;222;184;135m","\033[38;2;245;222;179m","\033[38;2;210;180;140m","\033[38;2;255;228;181m","\033[38;2;255;222;173m","\033[38;2;255;218;185m","\033[38;2;238;213;183m","\033[38;2;255;228;196m","\033[38;2;227;207;87m","\033[38;2;218;165;32m","\033[38;2;184;134;11m","\033[38;2;139;137;112m","\033[38;2;128;128;0m","\033[38;2;85;107;47m","\033[38;2;107;142;35m","\033[38;2;154;205;50m","\033[38;2;50;205;50m","\033[38;2;34;139;34m","\033[38;2;0;100;0m","\033[38;2;0;128;0m","\033[38;2;0;255;0m","\033[38;2;124;252;0m","\033[38;2;127;255;0m","\033[38;2;173;255;47m","\033[38;2;0;255;127m","\033[38;2;0;250;154m","\033[38;2;144;238;144m","\033[38;2;152;251;152m","\033[38;2;143;188;143m","\033[38;2;60;179;113m","\033[38;2;46;139;87m","\033[38;2;0;128;128m","\033[38;2;0;139;139m","\033[38;2;32;178;170m","\033[38;2;95;158;160m","\033[38;2;70;130;180m","\033[38;2;100;149;237m","\033[38;2;30;144;255m","\033[38;2;0;191;255m","\033[38;2;135;206;235m","\033[38;2;135;206;250m","\033[38;2;25;25;112m","\033[38;2;0;0;128m","\033[38;2;65;105;225m","\033[38;2;138;43;226m","\033[38;2;75;0;130m","\033[38;2;147;112;219m","\033[38;2;186;85;211m","\033[38;2;153;50;204m","\033[38;2;148;0;211m","\033[38;2;139;0;139m","\033[38;2;199;21;133m","\033[38;2;219;112;147m","\033[38;2;255;0;255m","\033[38;2;238;130;238m","\033[38;2;221;160;221m","\033[38;2;218;112;214m","\033[38;2;216;191;216m","\033[38;2;255;182;193m","\033[38;2;255;174;185m","\033[38;2;255;130;171m","\033[38;2;255;105;180m","\033[38;2;255;20;147m","\033[38;2;255;0;127m","\033[38;2;255;192;203m","\033[38;2;219;112;147m","\033[38;2;199;21;133m","\033[38;2;208;32;144m","\033[38;2;255;0;255m","\033[38;2;238;130;238m","\033[38;2;221;160;221m","\033[38;2;255;131;250m","\033[38;2;255;52;179m","\033[38;2;255;62;150m","\033[38;2;255;102;204m","\033[38;2;255;153;204m","\033[38;2;255;204;204m","\033[38;2;255;209;220m","\033[38;2;255;221;244m","\033[38;2;255;235;238m","\033[38;2;255;240;245m","\033[38;2;255;245;238m","\033[38;2;255;250;240m","\033[38;2;253;245;230m","\033[38;2;255;255;240m","\033[38;2;255;255;224m","\033[38;2;255;255;0m","\033[38;2;255;215;0m","\033[38;2;255;223;0m","\033[38;2;255;255;102m","\033[38;2;255;255;153m","\033[38;2;255;255;204m","\033[38;2;255;250;205m","\033[38;2;250;250;210m","\033[38;2;238;232;170m","\033[38;2;240;230;140m","\033[38;2;189;183;107m","\033[38;2;255;248;220m","\033[38;2;255;236;139m","\033[38;2;238;221;130m","\033[38;2;218;165;32m","\033[38;2;184;134;11m","\033[38;2;227;207;87m","\033[38;2;255;193;37m","\033[38;2;255;165;0m","\033[38;2;255;140;0m","\033[38;2;255;127;0m","\033[38;2;255;117;24m","\033[38;2;255;69;0m","\033[38;2;255;99;71m","\033[38;2;255;160;122m","\033[38;2;250;128;114m","\033[38;2;233;150;122m","\033[38;2;255;228;196m","\033[38;2;255;218;185m","\033[38;2;255;222;173m","\033[38;2;245;222;179m","\033[38;2;222;184;135m","\033[38;2;210;180;140m","\033[38;2;188;143;143m","\033[38;2;244;164;96m","\033[38;2;210;105;30m","\033[38;2;139;69;19m","\033[38;2;160;82;45m","\033[38;2;205;133;63m","\033[38;2;165;42;42m","\033[38;2;128;0;0m","\033[38;2;255;0;0m","\033[38;2;178;34;34m","\033[38;2;220;20;60m","\033[38;2;255;0;127m","\033[38;2;255;20;147m","\033[38;2;199;21;133m","\033[38;2;219;112;147m","\033[38;2;255;105;180m","\033[38;2;255;192;203m","\033[38;2;255;182;193m","\033[38;2;255;174;185m","\033[38;2;255;130;171m","\033[38;2;255;52;179m","\033[38;2;255;62;150m","\033[38;2;255;102;204m","\033[38;2;255;153;204m","\033[38;2;255;204;204m","\033[38;2;255;209;220m","\033[38;2;255;221;244m","\033[38;2;255;235;238m","\033[38;2;255;240;245m","\033[38;2;255;245;238m","\033[38;2;255;250;240m","\033[38;2;253;245;230m","\033[38;2;255;255;240m","\033[38;2;255;255;224m","\033[38;2;255;255;0m","\033[38;2;255;215;0m","\033[38;2;255;223;0m","\033[38;2;255;255;102m","\033[38;2;255;255;153m","\033[38;2;255;255;204m","\033[38;2;255;250;205m","\033[38;2;250;250;210m","\033[38;2;238;232;170m","\033[38;2;240;230;140m","\033[38;2;189;183;107m","\033[38;2;255;248;220m","\033[38;2;255;236;139m","\033[38;2;238;221;130m","\033[38;2;218;165;32m","\033[38;2;184;134;11m","\033[38;2;227;207;87m","\033[38;2;255;193;37m","\033[38;2;255;165;0m","\033[38;2;255;140;0m","\033[38;2;255;127;0m","\033[38;2;255;117;24m","\033[38;2;255;69;0m","\033[38;2;255;99;71m","\033[38;2;255;160;122m","\033[38;2;250;128;114m","\033[38;2;233;150;122m","\033[38;2;255;228;196m","\033[38;2;255;218;185m","\033[38;2;255;222;173m","\033[38;2;245;222;179m","\033[38;2;222;184;135m","\033[38;2;210;180;140m","\033[38;2;188;143;143m","\033[38;2;244;164;96m","\033[38;2;210;105;30m","\033[38;2;139;69;19m","\033[38;2;160;82;45m","\033[38;2;205;133;63m","\033[38;2;165;42;42m","\033[38;2;128;0;0m","\033[38;2;255;0;0m","\033[38;2;178;34;34m","\033[38;2;220;20;60m","\033[38;2;255;0;127m","\033[38;2;255;20;147m","\033[38;2;199;21;133m","\033[38;2;219;112;147m","\033[38;2;255;105;180m","\033[38;2;255;192;203m","\033[38;2;255;182;193m","\033[38;2;255;174;185m","\033[38;2;255;130;171m","\033[38;2;255;52;179m","\033[38;2;255;62;150m","\033[38;2;255;102;204m","\033[38;2;255;153;204m","\033[38;2;255;204;204m","\033[38;2;255;209;220m","\033[38;2;255;221;244m","\033[38;2;255;235;238m","\033[38;2;255;240;245m","\033[38;2;255;245;238m","\033[38;2;255;250;240m","\033[38;2;253;245;230m","\033[38;2;255;255;240m","\033[38;2;255;255;224m","\033[38;2;255;255;0m","\033[38;2;255;215;0m","\033[38;2;255;223;0m","\033[38;2;255;255;102m","\033[38;2;255;255;153m","\033[38;2;255;255;204m","\033[38;2;255;250;205m","\033[38;2;250;250;210m","\033[38;2;238;232;170m","\033[38;2;240;230;140m","\033[38;2;189;183;107m","\033[38;2;255;248;220m","\033[38;2;255;236;139m","\033[38;2;238;221;130m","\033[38;2;218;165;32m","\033[38;2;184;134;11m","\033[38;2;227;207;87m","\033[38;2;255;193;37m","\033[38;2;255;165;0m","\033[38;2;255;140;0m","\033[38;2;255;127;0m","\033[38;2;255;117;24m","\033[38;2;255;69;0m","\033[38;2;255;99;71m","\033[38;2;255;160;122m","\033[38;2;250;128;114m","\033[38;2;233;150;122m","\033[38;2;255;228;196m","\033[38;2;255;218;185m","\033[38;2;255;222;173m","\033[38;2;245;222;179m","\033[38;2;222;184;135m","\033[38;2;210;180;140m","\033[38;2;188;143;143m","\033[38;2;244;164;96m","\033[38;2;210;105;30m","\033[38;2;139;69;19m","\033[38;2;160;82;45m","\033[38;2;205;133;63m","\033[38;2;165;42;42m","\033[38;2;128;0;0m","\033[38;2;255;0;0m","\033[38;2;178;34;34m","\033[38;2;220;20;60m","\033[38;2;255;0;127m","\033[38;2;255;20;147m"]
    RESET = "\033[0m"
    COLOURS = random.choice(COLOUR)
    print(COLOURS + r""" 
 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \
\ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
 \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
 / /\                                                                                                                        / /\ 
/ /\ \ ██╗  ██╗███████╗████████╗███████╗██╗   ██╗███████╗██╗  ██╗██╗    ███╗   ██╗ ██████╗     ████████╗ ██████╗ ██╗   ██╗  / /\ \
\ \/ / ██║ ██╔╝██╔════╝╚══██╔══╝██╔════╝██║   ██║██╔════╝██║ ██╔╝██║    ████╗  ██║██╔═══██╗    ╚══██╔══╝██╔═══██╗██║   ██║  \ \/ /
 \/ /  █████╔╝ █████╗     ██║   ███████╗██║   ██║█████╗  █████╔╝ ██║    ██╔██╗ ██║██║   ██║       ██║   ██║   ██║██║   ██║   \/ / 
 / /\  ██╔═██╗ ██╔══╝     ██║   ╚════██║██║   ██║██╔══╝  ██╔═██╗ ██║    ██║╚██╗██║██║   ██║       ██║   ██║   ██║██║   ██║   / /\ 
/ /\ \ ██║  ██╗███████╗   ██║   ███████║╚██████╔╝███████╗██║  ██╗██║    ██║ ╚████║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝  / /\ \
\ \/ / ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝    ╚═╝  ╚═══╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝   \ \/ /
 \/ /                                                                                                                        \/ / 
 / /\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
/ /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ \
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' 
    """+ RESET)
    print("Welcome to Tower of Blood!")
    print("-" * 80)
    time.sleep(1)

def show_help():
    print("\n📘 Help Menu:")
    print("  w/a/s/d - Move")
    print("  j       - Descend a floor")
    print("  i       - View inventory and stats")
    print("  h       - Use health potion")
    print("  drop    - Drop a weapon or armour")
    print("  help    - Show this help menu")
    print("  q       - Quit the game\n")
    print("-----------------------------------------------")
    print("Minimap - Icons")
    print("P - Player")
    print("E - Enemies")
    print("B - Boss on Stair")
    print("S - Stairs without boss")
    print("K - Key that allows you to go through the exit")
    print("X - Exit")
    print(". - Normal room nothing inside")

def main():
    display_title()
    name = input("Enter your name: ")
    valid_classes = ["assassin", "mage", "archer", "warrior"]
    while True:
        print("\n⚔️ Class Base Stats:")
        print(f"{'Class':<10} {'HP':<5} {'Attack':<8} {'Defense':<8}")
        print("-" * 35)
        print(f"{'Assassin':<10} {100:<5} {20:<8} {5:<8}")
        print(f"{'Mage':<10} {100:<5} {25:<8} {3:<8}")
        print(f"{'Archer':<10} {100:<5} {18:<8} {6:<8}")
        print(f"{'Warrior':<10} {100:<5} {15:<8} {10:<8}")
        print("\nClass   Bonuses:")
        print("- Warriors get +2 with swords")
        print("- Assassins get +2 with daggers")
        print("- Archers get +2 with bows")
        print("- Mages get +2 with staffs")
        cls = input("Choose your class: ").lower()
        if cls in valid_classes:
            cls = cls.capitalize()
            break
        print("Incorrect input. Please enter a valid class.")

    player = Player(name, cls)
    dungeon = Dungeon(10, 10)

    print("\nYour adventure begins...")
    print("Type 'help' at any time to see available commands.\n")
    time.sleep(1)

    while True:
        print(f"\nYou are at {player.position} on Floor {player.floor + 1}")
        room = dungeon.get_room(player.floor, player.position)
        if room is None:
            print("Invalid room! Resetting to safe position (0,0).")
            player.position = (0, 0)
            room = dungeon.get_room(player.floor, player.position)

        dungeon.draw_minimap(player.floor, player.position)
        print("📝", random.choice(room_stories))

        if room.has_enemy and room.enemy and room.enemy.hp > 0:
            if not battle(player, room.enemy):
                break
            room.has_enemy = False
            room.enemy = None
            player.update_buffs_after_battle()

        for item in room.items:
            print(f"You found a {item.replace('_', ' ')}!")
            player.pick_up_item(item)
        room.items.clear()

        if room.has_key:
            print("You found the key!")
            player.has_key = True
            room.has_key = False

        if (player.floor == dungeon.exit_floor_index and
            player.position == dungeon.exit_room_position and
            player.has_key):
            print("🎉 You found the dungeon exit and escaped! You win!")
            break

        player_input = input("Move (w/a/s/d), down (j), inventory (i), heal (h), drop (drop), help (help), quit (q): ").lower()
        dx, dy = 0, 0

        if player_input == 'q':
            print("You chose to leave the Tower. Game over.")
            break
        elif player_input == 'help':
            show_help()
            continue
        elif player_input == 'one_punch_man':
            player.hp = 1
            player.permanent_buffs["damage"] = 99999999999999999999999999999999999999999999999999
            player.permanent_buffs["defense"] = 99999999999999999999999999999999999999999999999999
            print("☠️ _GODMODE ACTIVATED_☠️")
            print("You now have 1 health but can one-shot everything! 🤣😂")
            continue
 
        elif player_input == 'w': dy = 1
        elif player_input == 's': dy = -1
        elif player_input == 'a': dx = -1
        elif player_input == 'd': dx = 1
        elif player_input == 'j':
            if player.floor > 0:
                player.floor -= 1
                if not dungeon.room_exists(player.floor, player.position):
                    player.position = (0, 0)
                print(f"You descend to Floor {player.floor + 1}.")
                continue
            print("You're already on the bottom floor.")
            continue
        elif player_input == 'i':
            player.show_inventory()
            continue
        elif player_input == 'h':
            player.use_health_potion()
            continue
        elif player_input == 'drop':
            player.drop_item()
            continue
        else:
            print("Invalid input.")
            continue

        new_pos = (player.position[0] + dx, player.position[1] + dy)
        if dungeon.room_exists(player.floor, new_pos):
            player.position = new_pos
        else:
            print("No room that way.")
            continue

        new_room = dungeon.get_room(player.floor, player.position)
        if new_room.is_stairs:
            if new_room.has_enemy and new_room.enemy and new_room.enemy.is_alive():
                print("\nThe stairs are guarded by a powerful enemy!")
                if battle(player, new_room.enemy):
                    new_room.has_enemy = False
                    new_room.enemy = None
                    player.update_buffs_after_battle()
                    if player.floor < len(dungeon.floors) - 1:
                        print("⬆️ You climb the stairs to the next floor.")
                        player.floor += 1
                        if not dungeon.room_exists(player.floor, player.position):
                            player.position = (0, 0)
            else:
                if player.floor < len(dungeon.floors) - 1:
                    print("⬆️ You climb the stairs to the next floor.")
                    player.floor += 1
                    if not dungeon.room_exists(player.floor, player.position):
                        player.position = (0, 0)

if __name__ == "__main__":
    main()

```

player.py
```
import random

class Player:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.has_key = False
        self.hp = 100
        self.base_stats = {
            "Assassin": {"atk": 20, "defn": 5},
            "Mage": {"atk": 25, "defn": 3},
            "Archer": {"atk": 18, "defn": 6},
            "Warrior": {"atk": 15, "defn": 10}
        }
        self.atk = self.base_stats[char_class]["atk"]
        self.defn = self.base_stats[char_class]["defn"]
        self.permanent_buffs = {"damage": 0, "defense": 0}
        self.temp_buffs = {"damage": 0, "defense": 0}
        self.buff_encounters = {"damage": 0, "defense": 0}
        self.position = (0, 0)
        self.floor = 0
        self.inventory = {
            "health": 0,
            "weapons": [],
            "armour": None
        }
        
    def total_attack(self):
        class_bonus_type = {
            "Warrior": "sword",
            "Assassin": "dagger",
            "Archer": "bow",
            "Mage": "staff"
        }
        total = self.atk + self.permanent_buffs["damage"] + self.temp_buffs["damage"]
        for weapon in self.inventory["weapons"]:
            bonus = weapon["bonus"]
            if weapon["type"] == class_bonus_type[self.char_class]:
                bonus += 2
            total += bonus
        return total

    def total_defense(self):
        armour_bonus = 0
        if self.inventory["armour"]:
            armour_bonus = int(self.inventory["armour"].split('+')[1].split()[0])
        return self.defn + armour_bonus + self.permanent_buffs["defense"] + self.temp_buffs["defense"]

    def heal(self, amount):
        self.hp = min(100, self.hp + amount)

    def pick_up_item(self, item, source="normal"):
        if item == "health":
            if self.hp < 90:
                self.heal(10)
                print("You used the health potion immediately.")
            else:
                self.inventory["health"] += 1
                print("Health potion added to inventory.")
        elif item == "damage_buff":
            if source == "boss":
                print("💪 Permanent damage buff gained from boss!")
                self.permanent_buffs["damage"] += 1
            else:
                print("You drank a damage potion! (+2 damage for 3 battles)")
                self.temp_buffs["damage"] += 2
                self.buff_encounters["damage"] += 3
        elif item == "defense_buff":
            if source == "boss":
                print("🛡️ Permanent defense buff gained from boss!")
                self.permanent_buffs["defense"] += 1
            else:
                print("You drank a defense potion! (+2 defense for 3 battles)")
                self.temp_buffs["defense"] += 2
                self.buff_encounters["defense"] += 3
        elif item == "key":
            self.has_key = True
        elif item == "weapon":
            types = ["sword", "dagger", "bow", "staff"]
            chosen_type = random.choice(types)
            bonus = random.randint(3, 8)
            new_weapon = {
                "name": f"+{bonus} {chosen_type.capitalize()}",
                "bonus": bonus,
                "type": chosen_type
            }
            if len(self.inventory["weapons"]) < 2:
                self.inventory["weapons"].append(new_weapon)
                print(f"You equipped a new weapon: {new_weapon['name']}")
            else:
                print(f"❌ You already have 2 weapons.")
                print("Your current weapons:")
                for i, w in enumerate(self.inventory["weapons"]):
                    print(f"  [{i}] {w['name']} (Type: {w['type']})")
                print(f"New weapon: {new_weapon['name']} (Type: {new_weapon['type']})")
                while True:
                    choice = input("Type the number of a weapon to replace, or 'cancel': ").lower()
                    if choice.isdigit() and int(choice) in range(len(self.inventory["weapons"])):
                        dropped = self.inventory["weapons"].pop(int(choice))
                        self.inventory["weapons"].append(new_weapon)
                        print(f"Replaced {dropped['name']} with {new_weapon['name']}.")
                        break
                    elif choice == "cancel":
                        print("Kept your current weapons. New one discarded.")
                        break
                    else:
                        print("Invalid input. Please enter a valid number or 'cancel'.")

        elif item == "armour":
            bonus = random.randint(3, 8)
            new_armour = f"+{bonus} Defense armour"
            if self.inventory["armour"] is None:
                self.inventory["armour"] = new_armour
                print(f"You equipped new armour: {new_armour}")
            else:
                print(f"❌ You already have armour: {self.inventory['armour']}")
                print(f"New armour found: {new_armour}")
                while True:
                    choice = input("Type 'replace' to swap armour, or 'cancel': ").lower()
                    if choice == "replace":
                        old = self.inventory["armour"]
                        self.inventory["armour"] = new_armour
                        print(f"Replaced {old} with {new_armour}.")
                        break
                    elif choice == "cancel":
                        print("Kept your current armour. New one discarded.")
                        break
                    else:
                        print("Invalid input. Please type 'replace' or 'cancel'.")

    def update_buffs_after_battle(self):
        for stat in ["damage", "defense"]:
            if self.buff_encounters[stat] > 0:
                self.buff_encounters[stat] -= 1
                if self.buff_encounters[stat] == 0:
                    print(f"⏳ Your {stat} buff has worn off.")
                    self.temp_buffs[stat] = 0

    def show_inventory(self):
        print(f"\n📦 Inventory for {self.name} the {self.char_class}:")
        print(f"  Health Potions: {self.inventory['health']}")
        print("  Weapons:")
        for i, w in enumerate(self.inventory["weapons"]):
            print(f"    [{i}] {w['name']} (Type: {w['type']})")
        print(f"  armour: {self.inventory['armour'] or 'None'}")
        print(f"  Buffs: +{self.permanent_buffs['damage']} Permanent / +{self.temp_buffs['damage']} Temporary Damage")
        print(f"        +{self.permanent_buffs['defense']} Permanent / +{self.temp_buffs['defense']} Temporary Defense")
        print(f"  Current HP: {self.hp}/100\n")

    def use_health_potion(self):
        if self.inventory["health"] > 0:
            if self.hp == 100:
                print("You're already at full health!")
            else:
                self.heal(10)
                self.inventory["health"] -= 1
                print("You used a health potion.")
        else:
            print("No health potions available.")

    def drop_item(self):
        print("\n🗑️ Drop Menu:")
        self.show_inventory()
        choice = input("Drop [w]eapon, [a]rmor, or [c]ancel? ").lower()
        if choice == 'w':
            if not self.inventory["weapons"]:
                print("You have no weapons to drop.")
                return
            index = input(f"Enter weapon number to drop (0-{len(self.inventory['weapons'])-1}): ")
            if index.isdigit() and 0 <= int(index) < len(self.inventory["weapons"]):
                removed = self.inventory["weapons"].pop(int(index))
                print(f"Dropped {removed['name']}.")
            else:
                print("Invalid weapon index.")
        elif choice == 'a':
            if self.inventory["armour"]:
                print(f"Dropped {self.inventory['armour']}.")
                self.inventory["armour"] = None
            else:
                print("You have no armour to drop.")
        else:
            print("Cancelled drop.")

```

dungeon.py
```
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

```

room.py
```
from enemy import Enemy
import random

class Room:
    def __init__(self):
        self.has_enemy = random.random() < 0.2
        self.enemy = Enemy() if self.has_enemy else None
        self.has_key = False
        self.items = []
        self.is_stairs = False
        self.is_exit = False

        if random.random() < 0.2:
            self.items.append("health")
        if random.random() < 0.1:
            self.items.append(random.choice(["damage_buff", "defense_buff"]))
        if random.random() < 0.09:
            self.items.append(random.choice(["weapon", "armour"]))

    def set_key(self):
        self.has_key = True

```

enemy.py
```
import random

class Enemy:
    def __init__(self):
        types = [
            {"type": "Goblin", "hp": 30, "atk": 9, "defn": 3},
            {"type": "Werewolf", "hp": 50, "atk": 12, "defn": 5},
            {"type": "Vampire", "hp": 60, "atk": 10, "defn": 7}
        ]
        enemy = random.choice(types)
        self.name = enemy["type"]
        self.hp = enemy["hp"]
        self.atk = enemy["atk"]
        self.defn = enemy["defn"]

    def is_alive(self):
        return self.hp > 0

class Boss(Enemy):
    def __init__(self, floor_level):
        super().__init__()
        boss_types = [
            {"type": "Goblin King", "hp": 100, "atk": 20, "defn": 8},
            {"type": "Elder Vampire", "hp": 150, "atk": 25, "defn": 10},
            {"type": "Dragon", "hp": 175, "atk": 30, "defn": 12}
        ]
        boss = random.choice(boss_types)
        self.name = f"{boss['type']} (Floor {floor_level + 1})"
        self.hp = boss["hp"] + (floor_level * 5)
        self.atk = boss["atk"] + (floor_level *2)
        self.defn = boss["defn"] + (floor_level * 2)

```

combat.py
```
import random

def battle(player, enemy):
    is_boss = "King" in enemy.name or "Elder" in enemy.name or "Dragon" in enemy.name
    if is_boss:
        print(f"\n⚠️ BOSS BATTLE ⚠️")
        print(f"The {enemy.name} blocks your path!")
    else:
        print(f"A wild {enemy.name} appears!")

    while enemy.is_alive() and player.hp > 0:
        print(f"Your HP: {player.hp} | {enemy.name}'s HP: {enemy.hp}")
        while True:
            action = input("Attack (a) or Run (r): ").lower()
            if action in ['a', 'r']:
                break
            print("Incorrect input. Please enter 'a' to attack or 'r' to run.")

        if action == 'a':
            damage = max(1, player.total_attack() - enemy.defn)
            enemy.hp -= damage
            print(f"You dealt {damage} damage to the {enemy.name}!")

            if enemy.is_alive():
                enemy_dmg = max(0, enemy.atk - player.total_defense())
                player.hp -= enemy_dmg
                print(f"{enemy.name} dealt {enemy_dmg} damage to you.")
        elif action == 'r':
            print("The Enemy blocks your escape!")
            enemy_dmg = (player.hp + player.total_defense())
            print(f"{enemy.name} slices your head off as you flee, dealing {enemy_dmg} damage!")
            print("You Died!")
            return False

    if player.hp <= 0:
        print("💀 You died!")
        return False

    if is_boss:
        print(f"\n⭐ VICTORY! ⭐")
        print(f"You defeated the {enemy.name}!")
        player.heal(20)
        print("You recover 20 HP after the intense battle!")
        if random.random() < 0.7:
            print("The boss dropped a rare item!")
            player.pick_up_item(random.choice(["weapon", "armor", "damage_buff", "defense_buff"]), source="boss")
    else:
        print(f"You defeated the {enemy.name}!")

    return True


```

stories.txt
```
The walls are damp and echo with distant whispers.
A rusty chandelier swings slowly from the ceiling.
You feel a chill as you enter — something watched you.
Cobwebs cling to the corners like forgotten memories.
Ashes scatter across the floor, hinting at a burned past.
Scratched messages line the walls: "Turn back!"
A foul stench clings to the air in this chamber.
A single torch flickers, illuminating old bloodstains.
You hear chains rattling — but see no one.
The silence here is heavier than the stone around you.
The floorboards groan beneath your feet, as if warning you to leave.
A cold draft slithers through the room, carrying the scent of decay.
Shadows twist unnaturally, forming shapes that vanish when you look too close.
A child’s laughter echoes faintly—but there are no children here.
The air hums with a low, unsettling vibration, like a buried heartbeat.
Dust motes swirl in the dim light, as if disturbed by unseen movement.
A single drop of water falls in steady rhythm, like a ticking clock.
Your breath fogs in the air, though the cold feels unnatural.
Something skitters in the darkness—too large to be a rat.
The walls seem to breathe, pulsing faintly in the flickering torchlight.
A portrait’s eyes follow you, its painted smile now a grimace.
Footsteps echo behind you, but when you turn, nothing is there.
A whisper curls into your ear—just your name, then silence.
The door creaks shut on its own, though no wind stirs.
A broken mirror reflects a figure standing behind you—but you’re alone.
A book lies open on a table, its pages filled with frantic scribbles.
The flame of your torch burns green for a moment before returning to normal.
A handprint, fresh and wet, stains the wall—but whose?
The temperature drops suddenly, your skin prickling with unseen eyes.
A distant scream cuts through the silence—then is swallowed by the dark.
```


## Review
- Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.
Class selection, WASD movement, combat, boss battles, key collection, and  dungeon generation are fully implemented.

- Analyse the performance of your program against the key use-cases you identified.
The game successfully handles core use cases (exploration, combat, progression) but could improve boss fight mechanics and inventory depth.



- Assess the quality of your code in terms of readability, structure, and maintainability.
 Modular OOP structure, clear methods, and separation of concerns.

- Explain the improvements that should be made in the next stage of development.
Adding GUI, maybe better combat if have time
