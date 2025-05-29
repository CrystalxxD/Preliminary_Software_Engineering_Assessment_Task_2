from player import Player
from dungeon import Dungeon
from combat import battle

def main():
    name = input("Enter your name: ")
    cls = input("Choose your class (Assassin, Mage, Archer, Warrior): ").lower()
    player = Player(name, cls)
    dungeon = Dungeon(10, 10)

    while True:
        print(f"\nYou are at {player.position} on Floor {player.floor + 1}")
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
