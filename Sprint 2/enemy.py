import random

class Enemy:
    def __init__(self):
        types = [
            {"type": "Goblin", "hp": 30, "atk": 8, "defn": 3},
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
