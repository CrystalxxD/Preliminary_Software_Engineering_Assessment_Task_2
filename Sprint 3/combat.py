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
