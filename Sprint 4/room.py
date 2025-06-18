from enemy import Enemy, Boss
import random

class Room:
    def __init__(self, stories=None):
        # Reduced regular enemy spawn chance to 30%
        self.has_enemy = random.random() < 0.3
        if self.has_enemy:
            # Regular enemies only (bosses are handled in dungeon generation)
            self.enemy = Enemy()
        else:
            self.enemy = None
        self.has_key = False
        self.items = []
        self.is_stairs = False
        self.is_ascend = False  # New: Can ascend from this room
        self.is_descend = False  # New: Can descend from this room
        self.is_exit = False
        self.story = random.choice(stories) if stories else "A mysterious room."

        # Item generation with higher probabilities
        if random.random() < 0.4:  # 40% chance for health
            self.items.append("health")
        if random.random() < 0.3:  # 30% chance for buff
            self.items.append(random.choice(["damage_buff", "defense_buff"]))
        if random.random() < 0.2:  # 20% chance for equipment
            self.items.append(random.choice(["weapon", "armour"]))

    def set_key(self):
        self.has_key = True