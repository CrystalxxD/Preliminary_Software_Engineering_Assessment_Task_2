# Preliminary_Software_Engineering_Assessment_Task_2
# Sprint 1
### Requirements Definition
#### Functional Requirements

The game must allow the player to select a character class (e.g., Assassin, Warrior, Mage, Archer), each with unique stats. Players must navigate through at least 20 procedurally generated rooms across two dungeon floors using the WASD keys. Each room may contain enemies, items like potions or armor, or a key required to escape. Players must be able to fight enemies and bosses, pick up items, and track stats such as health, attack, and defense.

---
#### Non-Functional Requirements

The game should be responsive and user-friendly with simple controls. It must load quickly, have a clean text or GUI interface, and be built in Python using Object-Oriented Programming (OOP) principles. The final version should use a GUI (PySimpleGUI) and run without needing external game engines.

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

2.They move around using WASD keys, triggering stories in each room.

3. In some rooms, they find potions, buffs, or fight enemies.

4. They defeat enemies using their class stats and equipped items.

5. Upon finding the key and clearing most enemies, they move to Floor 2.

6. They eventually reach the final room, fight a boss, and escape.

Postconditions: Player wins if alive and reaches exit with key; loses if health reaches 0.

Exceptions: Player tries to move into walls; combat with enemies results in death.
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
``` bash
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
## Build and Test
[**Sprint 2 Folder**](<Sprint 2>)
- [main.py](<Sprint 2/main.py>)
- [enemy.py](<Sprint 2/enemy.py>)
- [dungeon.py](<Sprint 2/dungeon.py>)
- [player.py](<Sprint 2/player.py>)
- [combat.py](<Sprint 2/combat.py>)
- [room.py](<Sprint 2/room.py>)

## Review
