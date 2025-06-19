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
            "Warrior": {"atk": 150000, "defn": 10}
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
            "weapons": [],  # Only one weapon can be equipped
            "armour": None,  # Only one armor can be equipped
            "unequipped_weapons": [],
            "unequipped_armour": []
        }
        
    def total_attack(self):
        weapon_bonus = self.inventory["weapons"][0]["bonus"] if self.inventory["weapons"] else 0
        return self.atk + self.permanent_buffs["damage"] + self.temp_buffs["damage"] + weapon_bonus

    def total_defense(self):
        armour_bonus = int(self.inventory["armour"].split('+')[1].split()[0]) if self.inventory["armour"] else 0
        return self.defn + armour_bonus + self.permanent_buffs["defense"] + self.temp_buffs["defense"]

    def get_buff_status(self):
        status = []
        if self.permanent_buffs["damage"] > 0:
            status.append(f"Permanent +{self.permanent_buffs['damage']} Damage")
        if self.permanent_buffs["defense"] > 0:
            status.append(f"Permanent +{self.permanent_buffs['defense']} Defense")
        if self.temp_buffs["damage"] > 0:
            status.append(f"Temporary +{self.temp_buffs['damage']} Damage ({self.buff_encounters['damage']} fights left)")
        if self.temp_buffs["defense"] > 0:
            status.append(f"Temporary +{self.temp_buffs['defense']} Defense ({self.buff_encounters['defense']} fights left)")
        return status

    def heal(self, amount):
        self.hp = min(100, self.hp + amount)

    def pick_up_item(self, item, source="normal"):
        if item == "health":
            self.inventory["health"] += 1
            return "Health potion"
        elif item == "damage_buff":
            self.temp_buffs["damage"] += 1
            self.buff_encounters["damage"] = 2
            return "Temporary +1 Damage (next 2 fights)"
        elif item == "defense_buff":
            self.temp_buffs["defense"] += 1
            self.buff_encounters["defense"] = 2
            return "Temporary +1 Defense (next 2 fights)"
        elif item == "perm_damage":
            self.permanent_buffs["damage"] += 1
            return "PERMANENT +1 Damage"
        elif item == "perm_defense":
            self.permanent_buffs["defense"] += 1
            return "PERMANENT +1 Defense"
        elif item == "key":
            self.has_key = True
            return "Key"
        elif item == "weapon":
            types = ["sword", "dagger", "bow", "staff"]
            chosen_type = random.choice(types)
            bonus = random.randint(3, 8)
            new_weapon = {
                "name": f"+{bonus} {chosen_type.capitalize()}",
                "bonus": bonus,
                "type": chosen_type
            }
            self.inventory["unequipped_weapons"].append(new_weapon)
            return f"{new_weapon['name']} (added to inventory)"
        elif item == "armour":
            bonus = random.randint(3, 8)
            new_armour = f"+{bonus} Defense armour"
            self.inventory["unequipped_armour"].append(new_armour)
            return f"{new_armour} (added to inventory)"
        return "Unknown item"

    def equip_weapon(self, weapon_index):
        if weapon_index < 0 or weapon_index >= len(self.inventory["unequipped_weapons"]):
            return "Invalid weapon selection"
            
        weapon = self.inventory["unequipped_weapons"][weapon_index]
        
        # Unequip current weapon if exists
        if self.inventory["weapons"]:
            old_weapon = self.inventory["weapons"].pop()
            self.inventory["unequipped_weapons"].append(old_weapon)
        
        # Equip new weapon
        self.inventory["weapons"].append(weapon)
        self.inventory["unequipped_weapons"].pop(weapon_index)
        return f"Equipped {weapon['name']}"

    def equip_armour(self, armour_index):
        if armour_index < 0 or armour_index >= len(self.inventory["unequipped_armour"]):
            return "Invalid armour selection"
            
        armour = self.inventory["unequipped_armour"][armour_index]
        
        # Unequip current armor if exists
        if self.inventory["armour"]:
            old_armour = self.inventory["armour"]
            self.inventory["unequipped_armour"].append(old_armour)
        
        # Equip new armor
        self.inventory["armour"] = armour
        self.inventory["unequipped_armour"].pop(armour_index)
        return f"Equipped {armour}"

    def unequip_weapon(self):
        if not self.inventory["weapons"]:
            return "No weapon equipped"
        weapon = self.inventory["weapons"].pop()
        self.inventory["unequipped_weapons"].append(weapon)
        return f"Unequipped {weapon['name']}"

    def unequip_armour(self):
        if not self.inventory["armour"]:
            return "No armour equipped"
        armour = self.inventory["armour"]
        self.inventory["unequipped_armour"].append(armour)
        self.inventory["armour"] = None
        return f"Unequipped {armour}"

    def update_buffs_after_battle(self):
        for stat in ["damage", "defense"]:
            if self.buff_encounters[stat] > 0:
                self.buff_encounters[stat] -= 1
                if self.buff_encounters[stat] == 0:
                    self.temp_buffs[stat] = 0

    def use_health_potion(self):
        if self.inventory["health"] > 0 and self.hp < 100:
            self.heal(10)
            self.inventory["health"] -= 1
            return True
        return False