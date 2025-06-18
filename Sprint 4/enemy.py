import random

class Enemy:
    def __init__(self):
        types = [
            {
                "type": "Goblin", 
                "hp": 30, 
                "atk": 9, 
                "defn": 6, 
                "image": "Background Images/Goblin (enemies) Image.png",
                "color": (0, 128, 0),
                "attacks": [
                    {"name": "Club Swing", "multiplier": 1.0},
                    {"name": "Dirty Kick", "multiplier": 0.8},
                    {"name": "Headbutt", "multiplier": 1.2}
                ]
            },
            {
                "type": "Vampire", 
                "hp": 35, 
                "atk": 14, 
                "defn": 8, 
                "image": "Background Images/Vampire (enemies) Image.png",
                "color": (150, 0, 0),
                "attacks": [
                    {"name": "Blood Drain", "multiplier": 1.2},
                    {"name": "Shadow Strike", "multiplier": 1.0},
                    {"name": "Hypnotic Gaze", "multiplier": 0.8}
                ]
            },
            {
                "type": "Werewolf", 
                "hp": 40, 
                "atk": 16, 
                "defn": 9, 
                "image": "Background Images/Werewolf (enemies) Image.png",
                "color": (100, 50, 0),
                "attacks": [
                    {"name": "Claw Slash", "multiplier": 1.1},
                    {"name": "Bite", "multiplier": 1.3},
                    {"name": "Howl", "multiplier": 0.7}
                ]
            }
        ]
        enemy = random.choice(types)
        self.name = enemy["type"]
        self.hp = enemy["hp"]
        self.max_hp = enemy["hp"]
        self.atk = enemy["atk"]
        self.defn = enemy["defn"]
        self.image = enemy["image"]
        self.color = enemy["color"]
        self.attacks = enemy["attacks"]
        self.special_cooldown = 0
        self.last_damage_taken = 0

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        actual_damage = min(amount, self.hp)
        self.hp -= actual_damage
        self.last_damage_taken = actual_damage
        return actual_damage

    def perform_attack(self, player):
        attack = random.choice(self.attacks)
        base_damage = int(self.atk * attack["multiplier"])
        damage = max(0, base_damage - player.total_defense())
        player.hp -= damage
        
        return {
            "type": attack["name"],
            "damage": damage,
            "base_damage": base_damage,
            "message": f"{self.name} uses {attack['name']} ({base_damage} power)! " +
                      f"Your defense reduces it by {player.total_defense()}, taking {damage} damage!"
        }

class Boss(Enemy):
    def __init__(self, floor_level):
        super().__init__()
        boss_types = [
            {
                "type": "Kitsune", 
                "hp": 100, 
                "atk": 20, 
                "defn": 10,
                "ability": "Illusionary Clones",
                "ability_desc": "Creates 2 illusions that mimic attacks",
                "image": "Background Images/Kitsune Fox (boss) Image.png",
                "color": (255, 165, 0),
                "attacks": [
                    {"name": "Foxfire", "multiplier": 1.0},
                    {"name": "Tail Whip", "multiplier": 0.8},
                    {"name": "Spirit Blast", "multiplier": 1.5}
                ]
            },
            {
                "type": "Prince of Darkness", 
                "hp": 130, 
                "atk": 16, 
                "defn": 15,
                "ability": "Hellfire",
                "ability_desc": "Engulfs you in flames that ignore defense",
                "image": "Background Images/Demon (boss) Image.png",
                "color": (255, 50, 0),
                "attacks": [
                    {"name": "Infernal Strike", "multiplier": 1.3},
                    {"name": "Soul Burn", "multiplier": 1.1},
                    {"name": "Abyssal Slam", "multiplier": 1.5}
                ]
            },
            {
                "type": "Pitaya Dragon", 
                "hp": 160, 
                "atk": 32, 
                "defn": 16,
                "ability": "Dragon's Breath",
                "ability_desc": "Unleashes elemental fury on all enemies",
                "image": "Background Images/Dragon (boss) Image.png",
                "color": (0, 150, 150),
                "attacks": [
                    {"name": "Fire Breath", "multiplier": 1.4},
                    {"name": "Tail Swipe", "multiplier": 1.2},
                    {"name": "Wing Buffet", "multiplier": 1.1}
                ]
            }
        ]
        boss = random.choice(boss_types)
        self.name = f"{boss['type']} (Floor {floor_level + 1})"
        self.hp = boss["hp"] + (floor_level * 10)
        self.max_hp = self.hp
        self.atk = boss["atk"] + (floor_level * 4)
        self.defn = boss["defn"] + (floor_level * 3)
        self.special_ability = boss["ability"]
        self.ability_desc = boss["ability_desc"]
        self.image = boss["image"]
        self.color = boss["color"]
        self.attacks = boss["attacks"]
        self.special_cooldown = 0
        self.illusions = []

    def perform_attack(self, player):
        attack = random.choice(self.attacks)
        base_damage = int(self.atk * attack["multiplier"])
        defense_reduction = player.total_defense() / 4
        damage = max(1, base_damage - defense_reduction)
        
        return {
            "type": attack["name"],
            "damage": damage,
            "base_damage": base_damage,
            "message": f"{self.name} uses {attack['name']} ({base_damage} power)! " +
                    f"Your defense reduces it by {defense_reduction:.1f}, taking {damage} damage!"
        }

    def use_special_ability(self, player):
        self.special_cooldown = 3
        if self.special_ability == "Illusionary Clones":
            self.illusions = [{"hp": 1, "atk": self.atk // 2} for _ in range(2)]
            return {
                "type": "Illusionary Clones",
                "message": f"{self.name} creates 2 illusionary clones that will attack next turn!",
                "illusions": len(self.illusions)
            }
        elif self.special_ability == "Hellfire":
            damage = 25
            player.hp -= damage
            return {
                "type": "Hellfire",
                "damage": damage,
                "message": f"{self.name} engulfs you in hellfire for {damage} damage (ignores defense)!"
            }
        elif self.special_ability == "Dragon's Breath":
            damage = 30
            player.hp -= damage
            return {
                "type": "Dragon's Breath",
                "damage": damage,
                "message": f"{self.name} unleashes its elemental breath for {damage} devastating damage!"
            }