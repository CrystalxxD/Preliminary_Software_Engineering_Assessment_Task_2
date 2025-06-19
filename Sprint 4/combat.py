import pygame
import random
from enemy import Boss

def battle(player, enemy, gui):
    is_boss = isinstance(enemy, Boss)  # Check if the enemy is a boss
    
    if is_boss:
        gui.add_message(f"⚠️ BOSS BATTLE: {enemy.name} ⚠️")  # Display boss battle warning
        gui.add_message(f"Special Ability: {enemy.special_ability} - {enemy.ability_desc}")
    else:
        gui.add_message(f"A wild {enemy.name} appears!")  # Display regular enemy encounter

    while enemy.is_alive() and player.hp > 0:  # Continue battle until one is defeated
        action = gui.wait_for_input(['a', 'r'])  # Wait for player input (attack or run)
        
        if action == 'a':  # Player chooses to attack
            player_attack = player.total_attack()  # Calculate player's total attack power
            enemy_defense_reduction = enemy.defn  # Enemy's defense reduces damage
            damage = max(1, player_attack - enemy_defense_reduction)  # Ensure at least 1 damage
            damage_dealt = enemy.take_damage(damage)  # Apply damage to enemy
            
            gui.add_message(f"You attack with {player_attack} power!")
            gui.add_message(f"Enemy defense reduces it by {enemy_defense_reduction:.1f}")
            gui.add_message(f"You deal {damage_dealt} damage!")
            
            gui.draw_combat_screen(player, enemy)  # Update combat screen
            pygame.display.flip()
            pygame.time.delay(500)  # Pause for visual feedback
            
            if not enemy.is_alive():  # Check if enemy is defeated
                break
                
            # Enemy counterattack
            enemy_attack = enemy.perform_attack(player)  # Enemy attacks player
            player_defense_reduction = player.total_defense() / 4  # Player defense reduces damage
            enemy_damage = max(1, enemy_attack["damage"] - player_defense_reduction)
            player.hp -= enemy_damage  # Apply damage to player
            
            gui.add_message(f"{enemy.name} uses {enemy_attack['type']} attack!")
            gui.add_message(f"Your defense reduces it by {player_defense_reduction:.1f}")
            gui.add_message(f"You take {enemy_damage} damage!")
            
            if hasattr(enemy, 'illusions') and enemy.illusions:  # Handle boss illusions
                total_damage = 0
                for _ in enemy.illusions:
                    dmg = max(0, (enemy.atk//2) - (player.total_defense() / 4))
                    player.hp -= dmg
                    total_damage += dmg
                if total_damage > 0:
                    gui.add_message(f"{len(enemy.illusions)} illusions attack for {total_damage} total damage!")
                enemy.illusions = []  # Clear illusions after attack
                
        elif action == 'r':  # Player chooses to run
            if is_boss:
                damage = max(1, (player.hp // 2) - (player.total_defense() / 4))  # Boss deals heavy damage
                gui.add_message("The boss strikes you as you flee!")
            else:
                damage = max(1, enemy.atk - (player.total_defense() / 4))  # Regular enemy attack
                gui.add_message(f"{enemy.name} attacks as you flee!")
            player.hp -= damage
            gui.add_message(f"Your defense reduces it by {player.total_defense()/4:.1f}")
            gui.add_message(f"You take {damage} damage!")
            
            if player.hp <= 0:  # Check if player dies while fleeing
                gui.add_message("💀 You died!")
                return False
            return not is_boss  # Return whether escape was successful (cannot flee from boss)

    if player.hp <= 0:  # Player defeated
        gui.add_message("💀 You died!")
        return False

    if is_boss:  # Boss defeated
        gui.add_message(f"⭐ VICTORY! ⭐")
        player.heal(30)  # Reward: heal player
        # Boss drops permanent buff
        reward = random.choice(["perm_damage", "perm_defense"])
        result = player.pick_up_item(reward, source="boss")
        gui.add_message(f"Boss dropped: {result}")
    
    return True  # Player won the battle