import pygame
from pygame.locals import *
from windows import *
from enemy import Boss
from player import Player

pygame.font.init()
font_small = pygame.font.SysFont('Arial', 14)
font_medium = pygame.font.SysFont('Arial', 18)
font_large = pygame.font.SysFont('Arial', 24)

class GameState:
    def __init__(self):
        self.current_screen = "title"
        self.message_log = []
        self.max_messages = 10
        self.button_clicked = None
        self.show_help = False
        self.current_room_message = ""
        self.show_inventory = False
        self.inventory_scroll = 0

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.is_hovered = False
        
    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=5)
        
        text_surf = font_medium.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered

class GUI:
    def __init__(self, room_stories):
        self.room_stories = room_stories
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tower of Blood")
        self.state = GameState()
        self.buttons = self.create_buttons()
        self.enemy_images = {}
        self.title_image = self.load_background_image("Background Images/Title Page Background.png")
    
    def wait_for_input(self, valid_inputs):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if chr(event.key).lower() in valid_inputs:
                        return chr(event.key).lower()
                    if event.key == K_ESCAPE:
                        return 'r'
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    for button in [self.buttons["attack"], self.buttons["run"]]:
                        if button.rect.collidepoint(event.pos):
                            return button.action[-1]
            pygame.time.delay(100)
    
    def load_image(self, path):
        if path in self.enemy_images:
            return self.enemy_images[path]
            
        try:
            image = pygame.image.load(path).convert_alpha()
            self.enemy_images[path] = image
            return image
        except pygame.error:
            print(f"Failed to load enemy image: {path}")
            placeholder = pygame.Surface((300, 300), pygame.SRCALPHA)
            pygame.draw.rect(placeholder, (255, 0, 0, 128), (0, 0, 300, 300), 2)
            self.enemy_images[path] = placeholder
            return placeholder
    
    def load_background_image(self, path):
        try:
            image = pygame.image.load(path).convert()
            return pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except pygame.error:
            print(f"Failed to load background image: {path}")
            placeholder = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            placeholder.fill((50, 50, 50))
            return placeholder
    
    def add_message(self, message):
        self.state.message_log.append(message)
        if len(self.state.message_log) > self.state.max_messages:
            self.state.message_log.pop(0)
    
    def create_buttons(self):
        buttons = {
            "w": Button(GAME_AREA_WIDTH + STATS_AREA_WIDTH + 70, 550, 70, 50, "Up", LIGHT_GRAY, WHITE, "w"),
            "a": Button(GAME_AREA_WIDTH + STATS_AREA_WIDTH, 600, 70, 50, "Left", LIGHT_GRAY, WHITE, "a"),
            "s": Button(GAME_AREA_WIDTH + STATS_AREA_WIDTH + 70, 600, 70, 50, "Down", LIGHT_GRAY, WHITE, "s"),
            "d": Button(GAME_AREA_WIDTH + STATS_AREA_WIDTH + 140, 600, 70, 50, "Right", LIGHT_GRAY, WHITE, "d"),
            "k": Button(GAME_AREA_WIDTH + STATS_AREA_WIDTH, 550, 70, 50, "Ascend", LIGHT_GRAY, WHITE, "k"),
            "j": Button(GAME_AREA_WIDTH + STATS_AREA_WIDTH + 140, 550, 70, 50, "Descend", LIGHT_GRAY, WHITE, "j"),
            "i": Button(GAME_AREA_WIDTH + STATS_AREA_WIDTH, 400, 100, 40, "Inventory", LIGHT_GRAY, WHITE, "i"),
            "h": Button(GAME_AREA_WIDTH + STATS_AREA_WIDTH, 450, 100, 40, "Heal", LIGHT_GRAY, WHITE, "h"),
            "help": Button(GAME_AREA_WIDTH + STATS_AREA_WIDTH, 350, 100, 40, "Help", YELLOW, (255, 255, 150), "help"),
            "attack": Button(GAME_AREA_WIDTH//2 - 120, 600, 100, 40, "Attack", RED, (255, 100, 100), "attack"),
            "run": Button(GAME_AREA_WIDTH//2 + 20, 600, 100, 40, "Run", BLUE, (100, 100, 255), "run"),
            "start": Button(SCREEN_WIDTH//2 - 100, 400, 200, 50, "Start Game", GREEN, (100, 255, 100), "start"),
            "exit": Button(SCREEN_WIDTH//2 - 100, 470, 200, 50, "Exit", RED, (255, 100, 100), "exit"),
            "play_again": Button(SCREEN_WIDTH//2 - 100, 400, 200, 50, "Play Again", GREEN, (100, 255, 100), "start"),
            "quit": Button(SCREEN_WIDTH//2 - 100, 470, 200, 50, "Quit", RED, (255, 100, 100), "exit"),
            "warrior": Button(SCREEN_WIDTH//2 - 220, 300, 100, 40, "Warrior", BLUE, (100, 100, 255), "warrior"),
            "assassin": Button(SCREEN_WIDTH//2 - 110, 300, 100, 40, "Assassin", RED, (255, 100, 100), "assassin"),
            "mage": Button(SCREEN_WIDTH//2, 300, 100, 40, "Mage", PINK, (255, 150, 200), "mage"),
            "archer": Button(SCREEN_WIDTH//2 + 110, 300, 100, 40, "Archer", GREEN, (100, 255, 100), "archer"),
            "close_inv": Button(SCREEN_WIDTH//2 - 100, 650, 200, 40, "Close Inventory", RED, (255, 100, 100), "close_inv")
        }
        
        for i in range(6):
            x_pos = GAME_AREA_WIDTH + STATS_AREA_WIDTH + (i % 3) * 100
            y_pos = 200 + (i // 3) * 50
            buttons[f"inv_{i}"] = Button(x_pos, y_pos, 90, 40, f"Slot {i+1}", LIGHT_GRAY, WHITE, f"inv_{i}")
            
        return buttons
    
    def draw_title_screen(self, selected_class=None):
        self.screen.fill(BLACK)
        
        if self.title_image:
            self.screen.blit(self.title_image, (0, 0))
        
        title_text = font_large.render("TOWER OF BLOOD", True, RED)
        self.screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 200))
        
        if selected_class:
            class_text = font_medium.render(f"Selected: {selected_class}", True, WHITE)
            self.screen.blit(class_text, (SCREEN_WIDTH//2 - class_text.get_width()//2, 350))
        
        self.buttons["start"].draw(self.screen)
        self.buttons["exit"].draw(self.screen)
        for cls in ["warrior", "assassin", "mage", "archer"]:
            self.buttons[cls].draw(self.screen)
    
    def draw_help_menu(self):
        help_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        help_surface.fill((0, 0, 0, 200))
        self.screen.blit(help_surface, (0, 0))
        
        title = font_large.render("HELP / CONTROLS", True, YELLOW)
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 100))
        
        controls = [
            "Movement: W (Up), A (Left), S (Down), D (Right)",
            "Ascend Floor: K (when on stairs)",
            "Descend Floor: J (when on stairs)",
            "Inventory: I",
            "Use Health Potion: H",
            "Attack: A (in combat)",
            "Run: R (in combat)",
            "Close Help: Any key"
        ]
        
        y_pos = 200
        for control in controls:
            text = font_medium.render(control, True, WHITE)
            self.screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, y_pos))
            y_pos += 40
        
        instruction = font_medium.render("Press any key to return", True, YELLOW)
        self.screen.blit(instruction, (SCREEN_WIDTH//2 - instruction.get_width()//2, 500))
    
    def draw_inventory(self, player):
        inv_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        inv_surface.fill((0, 0, 0, 200))
        self.screen.blit(inv_surface, (0, 0))
        
        # Handle scrolling with mouse wheel
        for event in pygame.event.get():
            if event.type == pygame.MOUSEWHEEL:
                self.state.inventory_scroll -= event.y * 20
        
        # Limit scroll range
        max_scroll = max(0, (len(player.inventory["unequipped_weapons"]) + 
                        len(player.inventory["unequipped_armour"])) * 30 - 400)
        self.state.inventory_scroll = max(0, min(self.state.inventory_scroll, max_scroll))
        
        y_pos = 100 - self.state.inventory_scroll
        
        title = font_large.render("INVENTORY", True, YELLOW)
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, y_pos))
        y_pos += 50
        
        # Display buff status
        buff_status = player.get_buff_status()
        if buff_status:
            buff_title = font_medium.render("Active Buffs:", True, YELLOW)
            self.screen.blit(buff_title, (SCREEN_WIDTH//2 - 300, y_pos))
            y_pos += 30
            for buff in buff_status:
                buff_text = font_small.render(buff, True, WHITE)
                self.screen.blit(buff_text, (SCREEN_WIDTH//2 - 300, y_pos))
                y_pos += 25
            y_pos += 10
        
        # Equipped items
        equipped_title = font_medium.render("Equipped Items:", True, WHITE)
        self.screen.blit(equipped_title, (SCREEN_WIDTH//2 - 300, y_pos))
        y_pos += 30
        
        # Weapon slot
        if player.inventory["weapons"]:
            weapon = player.inventory["weapons"][0]
            weapon_text = font_small.render(f"Weapon: {weapon['name']}", True, WHITE)
            self.screen.blit(weapon_text, (SCREEN_WIDTH//2 - 300, y_pos))
            unequip_button = Button(SCREEN_WIDTH//2 + 100, y_pos - 5, 100, 25, "Unequip", RED, (255, 100, 100), "unequip_weapon")
            unequip_button.draw(self.screen)
            self.buttons["unequip_weapon"] = unequip_button
        else:
            weapon_text = font_small.render("Weapon: None", True, WHITE)
            self.screen.blit(weapon_text, (SCREEN_WIDTH//2 - 300, y_pos))
        y_pos += 30
        
        # Armor slot
        if player.inventory["armour"]:
            armour = player.inventory["armour"]
            armour_text = font_small.render(f"Armour: {armour}", True, WHITE)
            self.screen.blit(armour_text, (SCREEN_WIDTH//2 - 300, y_pos))
            unequip_button = Button(SCREEN_WIDTH//2 + 100, y_pos - 5, 100, 25, "Unequip", RED, (255, 100, 100), "unequip_armour")
            unequip_button.draw(self.screen)
            self.buttons["unequip_armour"] = unequip_button
        else:
            armour_text = font_small.render("Armour: None", True, WHITE)
            self.screen.blit(armour_text, (SCREEN_WIDTH//2 - 300, y_pos))
        y_pos += 40
        
        # Unequipped weapons
        if player.inventory["unequipped_weapons"]:
            weapons_text = font_medium.render("Unequipped Weapons:", True, WHITE)
            self.screen.blit(weapons_text, (SCREEN_WIDTH//2 - 300, y_pos))
            y_pos += 30
            
            for i, weapon in enumerate(player.inventory["unequipped_weapons"]):
                weapon_text = font_small.render(f"{i+1}. {weapon['name']}", True, WHITE)
                self.screen.blit(weapon_text, (SCREEN_WIDTH//2 - 300, y_pos))
                equip_button = Button(SCREEN_WIDTH//2 + 100, y_pos - 5, 80, 25, "Equip", GREEN, (100, 255, 100), f"equip_weapon_{i}")
                equip_button.draw(self.screen)
                self.buttons[f"equip_weapon_{i}"] = equip_button
                y_pos += 30
            y_pos += 10
        
        # Unequipped armour
        if player.inventory["unequipped_armour"]:
            armour_text = font_medium.render("Unequipped Armour:", True, WHITE)
            self.screen.blit(armour_text, (SCREEN_WIDTH//2 - 300, y_pos))
            y_pos += 30
            
            for i, armour in enumerate(player.inventory["unequipped_armour"]):
                armour_text = font_small.render(f"{i+1}. {armour}", True, WHITE)
                self.screen.blit(armour_text, (SCREEN_WIDTH//2 - 300, y_pos))
                equip_button = Button(SCREEN_WIDTH//2 + 100, y_pos - 5, 80, 25, "Equip", GREEN, (100, 255, 100), f"equip_armour_{i}")
                equip_button.draw(self.screen)
                self.buttons[f"equip_armour_{i}"] = equip_button
                y_pos += 30
            y_pos += 10
        
        # Potions
        potion_text = font_medium.render(f"Health Potions: {player.inventory['health']}", True, WHITE)
        self.screen.blit(potion_text, (SCREEN_WIDTH//2 - 300, y_pos))
        
        # Scroll indicator
        if max_scroll > 0:
            scroll_bar_height = 300
            scroll_bar_pos = (SCREEN_WIDTH - 20, 150 + (self.state.inventory_scroll/max_scroll) * scroll_bar_height)
            pygame.draw.rect(self.screen, WHITE, (SCREEN_WIDTH - 20, 150, 5, scroll_bar_height), 1)
            pygame.draw.rect(self.screen, WHITE, (SCREEN_WIDTH - 22, scroll_bar_pos[1], 9, 20))
        
        self.buttons["close_inv"].draw(self.screen)

    def draw_combat_messages(self):
        message_area = pygame.Surface((GAME_AREA_WIDTH - 40, 150))
        message_area.fill(DARK_GRAY)
        
        for i, msg in enumerate(self.state.message_log[-6:]):
            color = WHITE
            if any(word in msg.lower() for word in ["damage", "hit", "attack"]):
                color = RED
            elif "heal" in msg.lower():
                color = GREEN
            elif any(word in msg.lower() for word in ["ability", "special", "illusion"]):
                color = YELLOW
            
            msg_surface = font_medium.render(msg, True, color)
            message_area.blit(msg_surface, (10, 10 + i * 25))
        
        self.screen.blit(message_area, (20, 20))
    
    def draw_combat_screen(self, player, enemy):
        pygame.draw.rect(self.screen, DARK_GRAY, (0, 0, GAME_AREA_WIDTH, SCREEN_HEIGHT))
        
        enemy_img = self.load_image(enemy.image)
        if enemy_img:
            enemy_img = pygame.transform.scale(enemy_img, (300, 300))
            self.screen.blit(enemy_img, (GAME_AREA_WIDTH//2 - 150, 150))
        else:
            pygame.draw.rect(self.screen, RED, (GAME_AREA_WIDTH//2 - 150, 150, 300, 300), 2)
        
        self.draw_combat_messages()
        
        enemy_text = font_large.render(f"{enemy.name}", True, RED)
        hp_text = font_medium.render(f"HP: {enemy.hp}/{enemy.max_hp}", True, WHITE)
        self.screen.blit(enemy_text, (20, 470))
        self.screen.blit(hp_text, (20, 500))
        
        self.draw_animated_health_bar(enemy)
        
        self.draw_stats_area(player)
        
        self.buttons["attack"].draw(self.screen)
        self.buttons["run"].draw(self.screen)
    
    def draw_animated_health_bar(self, enemy):
        current_hp_ratio = enemy.hp / enemy.max_hp
        
        pygame.draw.rect(self.screen, BLACK, (20, 530, 300, 20))
        pygame.draw.rect(self.screen, RED, (20, 530, 300 * current_hp_ratio, 20))
        pygame.draw.rect(self.screen, BLACK, (20, 530, 300, 20), 2)
        
        if hasattr(enemy, 'last_damage_taken') and enemy.last_damage_taken > 0:
            damage_text = font_medium.render(f"-{enemy.last_damage_taken}", True, (255, 255, 0))
            damage_x = 20 + (300 * (enemy.hp + enemy.last_damage_taken) / enemy.max_hp)
            self.screen.blit(damage_text, (damage_x - damage_text.get_width()//2, 510))
    
    def draw_health_bar(self, current, max, x, y, w, h, color):
        ratio = current / max
        pygame.draw.rect(self.screen, BLACK, (x, y, w, h))
        pygame.draw.rect(self.screen, color, (x, y, w * ratio, h))
        pygame.draw.rect(self.screen, BLACK, (x, y, w, h), 2)
    
    def draw_stats_area(self, player):
        pygame.draw.rect(self.screen, GRAY, (GAME_AREA_WIDTH, 0, STATS_AREA_WIDTH, SCREEN_HEIGHT))
        
        stats = [
            f"Name: {player.name}",
            f"Class: {player.char_class}",
            f"Floor: {player.floor + 1}",
            f"HP: {player.hp}/100",
            f"Attack: {player.total_attack()}",
            f"Defense: {player.total_defense()}",
            f"Key: {'Yes' if player.has_key else 'No'}",
            f"Potions: {player.inventory['health']}"
        ]
        
        for i, stat in enumerate(stats):
            self.screen.blit(font_medium.render(stat, True, WHITE), (GAME_AREA_WIDTH + 20, 20 + i * 30))
    
    def draw_minimap(self, player, dungeon):
        pygame.draw.rect(self.screen, BLACK, (GAME_AREA_WIDTH + STATS_AREA_WIDTH, 0, MINIMAP_SIZE, MINIMAP_SIZE))
        if dungeon:
            dungeon.draw_pygame_minimap(self.screen, player.floor, player.position, 
                                     GAME_AREA_WIDTH + STATS_AREA_WIDTH, 0, MINIMAP_SIZE, MINIMAP_SIZE)
    
    def draw_action_buttons(self):
        for key in ['w', 'a', 's', 'd', 'k', 'j', 'i', 'h', 'help']:
            self.buttons[key].draw(self.screen)
    
    def draw_game_screen(self, player, dungeon):
        pygame.draw.rect(self.screen, DARK_GRAY, (0, 0, GAME_AREA_WIDTH, SCREEN_HEIGHT))
        
        for i, msg in enumerate(self.state.message_log):
            self.screen.blit(font_medium.render(msg, True, WHITE), (20, 20 + i * 25))
        
        room = dungeon.get_room(player.floor, player.position) if dungeon else None
        if room:
            self.draw_room_description(room)
        
        self.draw_stats_area(player)
        self.draw_minimap(player, dungeon)
        self.draw_action_buttons()
    
    def draw_room_description(self, room):
        self.state.message_log = [self.state.current_room_message]
        
        y_pos = 200
        words = room.story.split()
        current_line = ""
        
        for word in words:
            test_line = current_line + word + " "
            if font_medium.size(test_line)[0] < GAME_AREA_WIDTH - 40:
                current_line = test_line
            else:
                line_text = font_medium.render(current_line, True, WHITE)
                self.screen.blit(line_text, (20, y_pos))
                y_pos += 25
                current_line = word + " "
        
        if current_line:
            line_text = font_medium.render(current_line, True, WHITE)
            self.screen.blit(line_text, (20, y_pos))
            y_pos += 30
        
        if room.has_enemy and room.enemy and room.enemy.hp > 0:
            if isinstance(room.enemy, Boss):
                enemy_text = font_large.render(f"BOSS: {room.enemy.name}", True, PURPLE)
            else:
                enemy_text = font_large.render(f"Enemy: {room.enemy.name}", True, RED)
            self.screen.blit(enemy_text, (20, y_pos))
            y_pos += 40
        
        if room.is_ascend:
            if room.has_enemy and isinstance(room.enemy, Boss):
                stairs_text = font_medium.render("BOSS GUARDING ASCENDING STAIRS (press K)!", True, PURPLE)
            else:
                stairs_text = font_medium.render("There is an ascending staircase here (press K).", True, GREEN)
            self.screen.blit(stairs_text, (20, y_pos))
            y_pos += 30
        
        if room.is_descend:
            if room.has_enemy and isinstance(room.enemy, Boss):
                stairs_text = font_medium.render("BOSS GUARDING DESCENDING STAIRS (press J)!", True, PURPLE)
            else:
                stairs_text = font_medium.render("There is a descending staircase here (press J).", True, RED)
            self.screen.blit(stairs_text, (20, y_pos))
            y_pos += 30
        
        if room.has_key:
            key_text = font_medium.render("You see a shiny key!", True, YELLOW)
            self.screen.blit(key_text, (20, y_pos))
            y_pos += 30
        
        if room.is_exit:
            exit_text = font_large.render("THE EXIT!", True, GREEN)
            self.screen.blit(exit_text, (20, y_pos))
        
        if room.items:
            items_text = font_medium.render("Items here: " + ", ".join(room.items), True, (200, 200, 0))
            self.screen.blit(items_text, (20, y_pos))
    
    def update(self):
        pygame.display.flip()