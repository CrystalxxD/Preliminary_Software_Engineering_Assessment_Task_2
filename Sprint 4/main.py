import pygame
from pygame.locals import *
from gui import GUI
from player import Player
from dungeon import Dungeon
from windows import *
import os
from combat import battle

def load_stories():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        stories_path = os.path.join(script_dir, "stories.txt")
        with open(stories_path, "r", encoding='utf-8') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except Exception as e:
        print(f"Error loading stories: {e}")
        return ["A mysterious room."] * 20

def main():
    pygame.init()
    try:
        font_small = pygame.font.SysFont('Arial', 14)
        font_medium = pygame.font.SysFont('Arial', 18)
        font_large = pygame.font.SysFont('Arial', 24)
    except:
        print("Failed to initialize fonts")
        return

    room_stories = load_stories()
    gui = GUI(room_stories)
    player = None
    dungeon = None
    selected_class = None
    last_position = None
    last_room_message = ""
    clock = pygame.time.Clock()
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        if gui.state.current_screen == "title":
            active_buttons = ["warrior", "assassin", "mage", "archer", "start", "exit"]
        elif gui.state.current_screen == "game":
            if gui.state.show_inventory:
                active_buttons = ["close_inv"]
                if player:
                    if "unequip_weapon" in gui.buttons:
                        active_buttons.append("unequip_weapon")
                    if "unequip_armour" in gui.buttons:
                        active_buttons.append("unequip_armour")
                    for i in range(len(player.inventory["unequipped_weapons"])):
                        active_buttons.append(f"equip_weapon_{i}")
                    for i in range(len(player.inventory["unequipped_armour"])):
                        active_buttons.append(f"equip_armour_{i}")
            else:
                active_buttons = ["w", "a", "s", "d", "k", "j", "i", "h", "help", "e"]
                if player and dungeon:
                    room = dungeon.get_room(player.floor, player.position)
                    if room and room.has_enemy and room.enemy and room.enemy.hp > 0:
                        active_buttons.extend(["attack", "run"])

        for name, button in gui.buttons.items():
            button.is_hovered = False
            if name in active_buttons:
                button.check_hover(mouse_pos)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            if event.type == KEYDOWN and gui.state.show_help:
                gui.state.show_help = False
                continue
                
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked_button = None
                for name, button in gui.buttons.items():
                    if name in active_buttons and button.rect.collidepoint(event.pos):
                        clicked_button = button
                        break
                
                if clicked_button:
                    action = clicked_button.action
                    if action == "help":
                        gui.state.show_help = True
                    elif action in ["warrior", "assassin", "mage", "archer"]:
                        selected_class = action.capitalize()
                    elif action == "start" or action == "play_again":
                        if selected_class:
                            gui.state.current_screen = "game"
                            player = Player("Player", selected_class)
                            dungeon = Dungeon(10, 10, stories=room_stories)
                            last_position = None
                            last_room_message = ""
                            gui.state.message_log = []
                            gui.state.current_room_message = ""
                    elif action == "exit" or action == "quit":
                        running = False
                    elif action == "close_inv":
                        gui.state.show_inventory = False
                    elif action == "unequip_weapon":
                        result = player.unequip_weapon()
                        gui.add_message(result)
                    elif action == "unequip_armour":
                        result = player.unequip_armour()
                        gui.add_message(result)
                    elif action.startswith("equip_weapon_"):
                        try:
                            slot = int(action.split("_")[2])
                            result = player.equip_weapon(slot)
                            gui.add_message(result)
                        except (IndexError, ValueError):
                            gui.add_message("Invalid weapon selection")
                    elif action.startswith("equip_armour_"):
                        try:
                            slot = int(action.split("_")[2])
                            result = player.equip_armour(slot)
                            gui.add_message(result)
                        except (IndexError, ValueError):
                            gui.add_message("Invalid armour selection")
                    elif action in ["attack", "run"] and player and dungeon:
                        room = dungeon.get_room(player.floor, player.position)
                        if room and room.has_enemy and room.enemy and room.enemy.hp > 0:
                            if action == "attack":
                                if battle(player, room.enemy, gui):
                                    room.has_enemy = False
                                    room.enemy = None
                                    player.update_buffs_after_battle()
                                else:
                                    gui.state.current_screen = "title"
                                    player = None
                            elif action == "run":
                                damage = max(1, room.enemy.atk - player.total_defense())
                                player.hp -= damage
                                gui.add_message(f"{room.enemy.name} attacks as you flee!")
                                gui.add_message(f"You take {damage} damage!")
                                if player.hp <= 0:
                                    gui.state.current_screen = "title"
                                    player = None
                    elif player and dungeon:
                        if action in ['w', 'a', 's', 'd']:
                            room = dungeon.get_room(player.floor, player.position)
                            if room and room.has_enemy and room.enemy and room.enemy.hp > 0:
                                gui.add_message("You can't move while an enemy is present!")
                            else:
                                dx, dy = 0, 0
                                if action == 'w': dy = 1
                                elif action == 's': dy = -1
                                elif action == 'a': dx = -1
                                elif action == 'd': dx = 1
                                
                                new_pos = (player.position[0] + dx, player.position[1] + dy)
                                if dungeon.room_exists(player.floor, new_pos):
                                    player.position = new_pos
                        elif action == 'k':  # Ascend
                            room = dungeon.get_room(player.floor, player.position)
                            if room and room.is_ascend:
                                if player.floor < dungeon.exit_floor_index:
                                    player.floor += 1
                                    player.position = (0, 0)
                                    gui.add_message(f"You ascend to Floor {player.floor + 1}!")
                                    new_room = dungeon.get_room(player.floor, player.position)
                                    if new_room:
                                        gui.state.current_room_message = f"Entered room at {player.position} - {new_room.story}"
                        elif action == 'j':  # Descend
                            room = dungeon.get_room(player.floor, player.position)
                            if room and room.has_enemy and room.enemy and room.enemy.hp > 0:
                                gui.add_message("You must defeat the enemy before descending!")
                            else:
                                if player.floor > 0:
                                    player.floor -= 1
                                    if not dungeon.room_exists(player.floor, player.position):
                                        player.position = (0, 0)
                                    gui.add_message(f"You descend to Floor {player.floor + 1}!")
                                    new_room = dungeon.get_room(player.floor, player.position)
                                    if new_room:
                                        gui.state.current_room_message = f"Entered room at {player.position} - {new_room.story}"
                                else:
                                    gui.add_message("You can't descend from the bottom floor!")
                        elif action == 'h':
                            if player.use_health_potion():
                                gui.add_message("You used a health potion (+10 HP).")
                            else:
                                gui.add_message("No health potions available or already at full health!")
                        elif action == 'i':
                            gui.state.show_inventory = True
                        elif action == 'e':  # Exit interaction
                            room = dungeon.get_room(player.floor, player.position)
                            if room and room.is_exit:
                                if player.has_key:
                                    gui.add_message("⭐ YOU ESCAPED THE TOWER! ⭐")
                                    pygame.time.delay(2000)
                                    gui.state.current_screen = "title"
                                    player = None
                                else:
                                    gui.add_message("You need the golden key to unlock the exit!")
            
            if event.type == KEYDOWN and gui.state.current_screen == "game" and player and dungeon:
                if event.key == K_h:
                    if player.use_health_potion():
                        gui.add_message("You used a health potion (+10 HP).")
                    else:
                        gui.add_message("No health potions available or already at full health!")
                elif event.key == K_QUESTION:
                    gui.state.show_help = True
                elif event.key == K_k:  # Ascend
                    room = dungeon.get_room(player.floor, player.position)
                    if room and room.is_ascend:
                        if player.floor < dungeon.exit_floor_index:
                            player.floor += 1
                            player.position = (0, 0)
                            gui.add_message(f"You ascend to Floor {player.floor + 1}!")
                            new_room = dungeon.get_room(player.floor, player.position)
                            if new_room:
                                gui.state.current_room_message = f"Entered room at {player.position} - {new_room.story}"
                elif event.key == K_j:  # Descend
                    room = dungeon.get_room(player.floor, player.position)
                    if room and room.has_enemy and room.enemy and room.enemy.hp > 0:
                        gui.add_message("You must defeat the enemy before descending!")
                    else:
                        if player.floor > 0:
                            player.floor -= 1
                            if not dungeon.room_exists(player.floor, player.position):
                                player.position = (0, 0)
                            gui.add_message(f"You descend to Floor {player.floor + 1}!")
                            new_room = dungeon.get_room(player.floor, player.position)
                            if new_room:
                                gui.state.current_room_message = f"Entered room at {player.position} - {new_room.story}"
                        else:
                            gui.add_message("You can't descend from the bottom floor!")
                elif event.key == K_e:  # Exit interaction
                    room = dungeon.get_room(player.floor, player.position)
                    if room and room.is_exit:
                        if player.has_key:
                            gui.add_message("⭐ YOU ESCAPED THE TOWER! ⭐")
                            pygame.time.delay(2000)
                            gui.state.current_screen = "title"
                            player = None
                        else:
                            gui.add_message("You need the golden key to unlock the exit!")
                else:
                    room = dungeon.get_room(player.floor, player.position)
                    if room and room.has_enemy and room.enemy and room.enemy.hp > 0:
                        if event.key == K_a:
                            if battle(player, room.enemy, gui):
                                room.has_enemy = False
                                room.enemy = None
                                player.update_buffs_after_battle()
                            else:
                                gui.state.current_screen = "title"
                        elif event.key == K_r or event.key == K_ESCAPE:
                            damage = max(1, room.enemy.atk - player.total_defense())
                            player.hp -= damage
                            gui.add_message(f"{room.enemy.name} attacks as you flee!")
                            gui.add_message(f"You take {damage} damage!")
                            if player.hp <= 0:
                                gui.state.current_screen = "title"
                    else:
                        dx, dy = 0, 0
                        if event.key == K_w: dy = 1
                        elif event.key == K_s: dy = -1
                        elif event.key == K_a: dx = -1
                        elif event.key == K_d: dx = 1
                        
                        if dx != 0 or dy != 0:
                            new_pos = (player.position[0] + dx, player.position[1] + dy)
                            if dungeon.room_exists(player.floor, new_pos):
                                player.position = new_pos
        
        if player and dungeon:
            if player.position != last_position:
                room = dungeon.get_room(player.floor, player.position)
                if room:
                    last_room_message = f"Entered room at {player.position} - {room.story}"
                    gui.state.current_room_message = last_room_message
                    last_position = player.position
                    
                    if room.items:
                        found_items = []
                        for item in room.items[:]:
                            if item == "key" and player.has_key:
                                continue
                            result = player.pick_up_item(item)
                            if result:
                                found_items.append(result)
                                room.items.remove(item)
                                if item == "key":
                                    room.has_key = False
                        
                        if found_items:
                            items_message = "You found: " + ", ".join(found_items)
                            gui.add_message(items_message)
        
        gui.screen.fill(BLACK)
        
        if gui.state.show_help:
            gui.draw_help_menu()
        elif gui.state.current_screen == "title":
            gui.draw_title_screen(selected_class)
        elif gui.state.current_screen == "game":
            if player and dungeon:
                if player.hp <= 0:
                    gui.state.current_screen = "title"
                    player = None
                else:
                    if gui.state.show_inventory:
                        gui.draw_inventory(player)
                    else:
                        room = dungeon.get_room(player.floor, player.position)
                        if room and room.has_enemy and room.enemy and room.enemy.hp > 0:
                            gui.draw_combat_screen(player, room.enemy)
                        else:
                            gui.draw_game_screen(player, dungeon)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()