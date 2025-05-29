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