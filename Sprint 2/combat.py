def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while enemy.is_alive() and player.hp > 0:
        print(f"Your HP: {player.hp} | {enemy.name}'s HP: {enemy.hp}")
        action = input("Attack (a) or Run (r): ").lower()
        if action == 'a':
            damage = max(0, player.total_attack() - enemy.defn)
            enemy.hp -= damage
            print(f"You dealt {damage} damage to the {enemy.name}!")

            if enemy.is_alive():
                enemy_dmg = max(0, enemy.atk - player.total_defense())
                player.hp -= enemy_dmg
                print(f"{enemy.name} dealt {enemy_dmg} damage to you.")
        elif action == 'r':
            print("You escaped!")
            return False

    if player.hp <= 0:
        print("You died!")
        return False
    else:
        print(f"You defeated the {enemy.name}!")
        return True
