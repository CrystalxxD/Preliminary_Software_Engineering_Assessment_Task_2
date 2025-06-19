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
                "attacks": [  # Different attack types with multipliers
                    {"name": "Club Swing", "multiplier": 1.0},
                    {"name": "Dirty Kick", "multiplier": 0.8},
                    {"name": "Headbutt", "multiplier": 1.2}
                ]
            },
            # Other enemy types (Vampire, Werewolf) follow similar structure
        ]
        enemy = random.choice(types)  # Randomly select enemy type
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
        return self.hp > 0  # Check if enemy is alive

    def take_damage(self, amount):
        actual_damage = min(amount, self.hp)  # Ensure HP doesn't go negative
        self.hp -= actual_damage
        self.last_damage_taken = actual_damage  # Track last damage for visual feedback
        return actual_damage

    def perform_attack(self, player):
        attack = random.choice(self.attacks)  # Randomly select attack
        base_damage = int(self.atk * attack["multiplier"])  # Calculate base damage
        damage = max(0, base_damage - player.total_defense())  # Apply player defense
        player.hp -= damage  # Deal damage to player
        
        return {
            "type": attack["name"],
            "damage": damage,
            "base_damage": base_damage,
            "message": f"{self.name} uses {attack['name']} ({base_damage} power)! " +
                      f"Your defense reduces it by {player.total_defense()}, taking {damage} damage!"
        }

class Boss(Enemy):  # Inherits from Enemy
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
            # Other boss types (Prince of Darkness, Pitaya Dragon) follow similar structure
        ]
        boss = random.choice(boss_types)
        self.name = f"{boss['type']} (Floor {floor_level + 1})"  # Include floor number in name
        self.hp = boss["hp"] + (floor_level * 10)  # Scale HP with floor level
        self.max_hp = self.hp
        self.atk = boss["atk"] + (floor_level * 4)  # Scale attack with floor level
        self.defn = boss["defn"] + (floor_level * 3)  # Scale defense with floor level
        self.special_ability = boss["ability"]
        self.ability_desc = boss["ability_desc"]
        self.image = boss["image"]
        self.color = boss["color"]
        self.attacks = boss["attacks"]
        self.special_cooldown = 0
        self.illusions = []  # For Kitsune's special ability

    def perform_attack(self, player):
        attack = random.choice(self.attacks)
        base_damage = int(self.atk * attack["multiplier"])
        defense_reduction = player.total_defense() / 4  # Boss attacks ignore some defense
        damage = max(1, base_damage - defense_reduction)
        
        return {
            "type": attack["name"],
            "damage": damage,
            "base_damage": base_damage,
            "message": f"{self.name} uses {attack['name']} ({base_damage} power)! " +
                    f"Your defense reduces it by {defense_reduction:.1f}, taking {damage} damage!"
        }

    def use_special_ability(self, player):
        self.special_cooldown = 3  # Cooldown for special ability
        if self.special_ability == "Illusionary Clones":
            self.illusions = [{"hp": 1, "atk": self.atk // 2} for _ in range(2)]  # Create illusions
            return {
                "type": "Illusionary Clones",
                "message": f"{self.name} creates 2 illusionary clones that will attack next turn!",
                "illusions": len(self.illusions)
            }
        elif self.special_ability == "Hellfire":
            damage = 25  # Fixed damage ignoring defense
            player.hp -= damage
            return {
                "type": "Hellfire",
                "damage": damage,
                "message": f"{self.name} engulfs you in hellfire for {damage} damage (ignores defense)!"
            }
        elif self.special_ability == "Dragon's Breath":
            damage = 30  # Heavy fixed damage
            player.hp -= damage
            return {
                "type": "Dragon's Breath",
                "damage": damage,
                "message": f"{self.name} unleashes its elemental breath for {damage} devastating damage!"
            }