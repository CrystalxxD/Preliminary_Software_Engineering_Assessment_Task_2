from enemy import Enemy, Boss
import random

class Room:
    def __init__(self, stories=None):
        self.has_enemy = random.random() < 0.3
        if self.has_enemy:
            self.enemy = Enemy()
        else:
            self.enemy = None
        self.has_key = False
        self.items = []
        self.is_stairs = False
        self.is_ascend = False
        self.is_descend = False
        self.is_exit = False
        self.story = random.choice(stories) if stories else "A mysterious room."

        if not self.is_exit:  # Only generate items in non-exit rooms
            if random.random() < 0.4:
                self.items.append("health")
            if random.random() < 0.3:
                self.items.append(random.choice(["damage_buff", "defense_buff"]))
            if random.random() < 0.2:
                self.items.append(random.choice(["weapon", "armour"]))

    def set_key(self):
        self.has_key = True
        self.items.append("key")