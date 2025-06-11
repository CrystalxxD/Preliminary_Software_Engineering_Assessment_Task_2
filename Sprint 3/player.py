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