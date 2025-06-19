import pygame
import random
from enemy import Boss

def battle(player, enemy, gui):
    is_boss = isinstance(enemy, Boss)
    
    if is_boss:
        gui.add_message(f"⚠️ BOSS BATTLE: {enemy.name} ⚠️")
        gui.add_message(f"Special Ability: {enemy.special_ability} - {enemy.ability_desc}")
    else:
        gui.add_message(f"A wild {enemy.name} appears!")

    while enemy.is_alive() and player.hp > 0:
        action = gui.wait_for_input(['a', 'r'])
        
        if action == 'a':
            player_attack = player.total_attack()
            enemy_defense_reduction = enemy.defn
            damage = max(1, player_attack - enemy_defense_reduction)
            damage_dealt = enemy.take_damage(damage)
            
            gui.add_message(f"You attack with {player_attack} power!")
            gui.add_message(f"Enemy defense reduces it by {enemy_defense_reduction:.1f}")
            gui.add_message(f"You deal {damage_dealt} damage!")
            
            gui.draw_combat_screen(player, enemy)
            pygame.display.flip()
            pygame.time.delay(500)
            
            if not enemy.is_alive():
                break
                
            # Enemy attack (player defense divided by 4)
            enemy_attack = enemy.perform_attack(player)
            player_defense_reduction = player.total_defense() / 4
            enemy_damage = max(1, enemy_attack["damage"] - player_defense_reduction)
            player.hp -= enemy_damage
            
            gui.add_message(f"{enemy.name} uses {enemy_attack['type']} attack!")
            gui.add_message(f"Your defense reduces it by {player_defense_reduction:.1f}")
            gui.add_message(f"You take {enemy_damage} damage!")
            
            if hasattr(enemy, 'illusions') and enemy.illusions:
                total_damage = 0
                for _ in enemy.illusions:
                    dmg = max(0, (enemy.atk//2) - (player.total_defense() / 4))
                    player.hp -= dmg
                    total_damage += dmg
                if total_damage > 0:
                    gui.add_message(f"{len(enemy.illusions)} illusions attack for {total_damage} total damage!")
                enemy.illusions = []
                
        elif action == 'r':
            if is_boss:
                damage = max(1, (player.hp // 2) - (player.total_defense() / 4))
                gui.add_message("The boss strikes you as you flee!")
            else:
                damage = max(1, enemy.atk - (player.total_defense() / 4))
                gui.add_message(f"{enemy.name} attacks as you flee!")
            player.hp -= damage
            gui.add_message(f"Your defense reduces it by {player.total_defense()/4:.1f}")
            gui.add_message(f"You take {damage} damage!")
            
            if player.hp <= 0:
                gui.add_message("💀 You died!")
                return False
            return not is_boss

    if player.hp <= 0:
        gui.add_message("💀 You died!")
        return False

    if is_boss:
        gui.add_message(f"⭐ VICTORY! ⭐")
        player.heal(30)
        # Bosses always give permanent buffs
        reward = random.choice(["perm_damage", "perm_defense"])
        result = player.pick_up_item(reward, source="boss")
        gui.add_message(f"Boss dropped: {result}")
    
    return True