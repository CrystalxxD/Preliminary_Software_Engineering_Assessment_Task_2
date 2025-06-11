from enemy import Enemy
import random

class Room:
    def __init__(self):
        self.has_enemy = random.random() < 0.2
        self.enemy = Enemy() if self.has_enemy else None
        self.has_key = False
        self.items = []
        self.is_stairs = False
        self.is_exit = False

        if random.random() < 0.2:
            self.items.append("health")
        if random.random() < 0.1:
            self.items.append(random.choice(["damage_buff", "defense_buff"]))
        if random.random() < 0.09:
            self.items.append(random.choice(["weapon", "armour"]))

    def set_key(self):
        self.has_key = True