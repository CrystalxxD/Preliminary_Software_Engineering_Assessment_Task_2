import random

class Player:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.has_key = False
        self.hp = 100
        self.base_stats = {
            "assassin": {"atk": 20, "defn": 5},
            "mage": {"atk": 25, "defn": 3},
            "archer": {"atk": 18, "defn": 6},
            "warrior": {"atk": 15, "defn": 10}
        }
        self.atk = self.base_stats[char_class]["atk"]
        self.defn = self.base_stats[char_class]["defn"]
        self.weapon_bonus = 0
        self.armour_bonus = 0
        self.buffs = {"damage": 0, "defense": 0}
        self.position = (0, 0)
        self.floor = 0


    def total_attack(self):
        return self.atk + self.weapon_bonus + self.buffs["damage"]

    def total_defense(self):
        return self.defn + self.armour_bonus + self.buffs["defense"]

    def heal(self, amount):
        self.hp = min(100, self.hp + amount)

    def pick_up_item(self, item):
        if item == "health":
            self.heal(30)
        elif item == "damage_buff":
            self.buffs["damage"] += 5
        elif item == "defense_buff":
            self.buffs["defense"] += 5
        elif item == "key":
            self.has_key = True
        elif item == "weapon":
            self.weapon_bonus = random.randint(3, 8)
        elif item == "armour":
            self.armour_bonus = random.randint(3, 8)
