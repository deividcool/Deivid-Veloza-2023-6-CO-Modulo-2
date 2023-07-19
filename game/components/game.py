import pygame

from game.utils.constants import BG,ICON, SCREEN_HEIGHT, SCREEN_WIDTH ,  TITLE, FPS, FONT_STYLE, DEFAULT_TYPE,COMBAT, INTRO
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menus.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.high_score = {'high_score': 0, 'death_count':0}
        self.menu = Menu('Press any key to start...', self.screen)
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.playing = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.shield = False
        self.lifes = 3
        self.lives_images = []
        self.life_image = pygame.transform.scale(ICON, (30, 30))
        

        for _ in range(self.lifes):
            self.lives_images.append(self.life_image)

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.enemy_manager.reset()
        self.lifes = 3
        self.lives_images = []
        self.life_image = pygame.transform.scale(ICON, (30, 30))
        for _ in range(self.lifes):
            self.lives_images.append(self.life_image)
        self.score = 0
        self.menu.reset_message()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_iput = pygame.key.get_pressed()
        self.player.update(user_iput,self)
        self.enemy_manager.update(self.bullet_manager)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))

        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        self.draw_life()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset_screen_collor(self.screen)
        half_screen_heigth = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            self.menu.update_message(f'You Score:  {self.score}', 40)  
            self.menu.update_message(f'Highest score: {int(self.high_score["high_score"])}', 70)
            self.menu.update_message(f'Total deaths: {int(self.high_score["death_count"])}', 100) 
            self.menu.draw(self.screen)
            
            for text, rect in self.menu.texts:
                self.screen.blit(text, rect)

        icon = pygame.transform.scale(ICON, (80, 120))
        self.screen.blit(icon, (half_screen_width - 50, half_screen_heigth - 150))

        self.menu.update(self)
    
    def update_score(self):
        self.score += 1
        self.high_score['score']= self.score

        if self.score > self.high_score['high_score']:
            self.high_score['high_score'] = self.score
            self.high_score['death_count'] = self.death_count
        
    def update_death_count(self):
        self.death_count += 1
        self.high_score['death_count'] = self.death_count

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_life(self):
        x = 20  
        y = 20 
    
        for life_image in self.lives_images:
            self.screen.blit(life_image, (x, y))
            x += 35
    
    def remove_life_image(self):
        if self.lifes > 0:
            self.lifes -= 1
            self.lives_images.pop()

    def add_life_image(self):
        self.lifes += 1
        self.lives_images.append(self.life_image)

