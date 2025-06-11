import random

class Enemy:
    def __init__(self):
        types = [
            {"type": "Goblin", "hp": 30, "atk": 9, "defn": 3},
            {"type": "Werewolf", "hp": 50, "atk": 12, "defn": 5},
            {"type": "Vampire", "hp": 60, "atk": 10, "defn": 7}
        ]
        enemy = random.choice(types)
        self.name = enemy["type"]
        self.hp = enemy["hp"]
        self.atk = enemy["atk"]
        self.defn = enemy["defn"]

    def is_alive(self):
        return self.hp > 0

class Boss(Enemy):
    def __init__(self, floor_level):
        super().__init__()
        boss_types = [
            {"type": "Goblin King", "hp": 100, "atk": 20, "defn": 8},
            {"type": "Elder Vampire", "hp": 150, "atk": 25, "defn": 10},
            {"type": "Dragon", "hp": 175, "atk": 30, "defn": 12}
        ]
        boss = random.choice(boss_types)
        self.name = f"{boss['type']} (Floor {floor_level + 1})"
        self.hp = boss["hp"] + (floor_level * 5)
        self.atk = boss["atk"] + (floor_level *2)
        self.defn = boss["defn"] + (floor_level * 2)