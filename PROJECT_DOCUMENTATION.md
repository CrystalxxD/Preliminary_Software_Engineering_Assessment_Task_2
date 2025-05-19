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
![Alt text](Images/Text%20Based%20Game%20Story%20Board.png)
![Alt text](Images/Gui%20of%20Story%20Board.png)
---

## Build and Test
In Sprint 1 Folder

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