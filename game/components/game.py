import pygame
import pickle

from game.utils.constants import BG, ICON, GAMEOVER, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menus.menu import Menu
from game.components.counts.counter import Counter
from game.components.counts.leader_board import LeaderBoard
from game.components.power_ups.power_up_manager import PowerUpManager 
from game.components.power_ups.hearts import Hearts  

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        pygame.display.set_icon(GAMEOVER)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu(self.screen)
        self.score = Counter()
        self.death_count = Counter()
        self.leader_board = LeaderBoard()
        self.heart = Hearts()
        self.show_leader_board = False
        self.power_up_manager = PowerUpManager()

        
    def execute(self):
        self.load_high_score()
        self.running = True
        while self.running:
            if not self.playing and not self.show_leader_board:
                self.show_menu()
            elif self.show_leader_board:
                self.show_higest_scores()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.reset()
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
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self.bullet_manager)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.score.draw(self.screen, 'Score', (1000, 50))
        self.heart.draw(self.screen)
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
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        icon = self.image = pygame.transform.scale(ICON, (80, 120))
        imageGameOver = self.image = pygame.transform.scale(GAMEOVER, (300, 120))
        self.menu.reset(self.screen)

        if self.death_count.count == 0:
            self.screen.blit(icon, (half_screen_width - 50, half_screen_height - 150))
            self.menu.draw(self.screen, 'Press any key to start ...')
        else:
            self.screen.blit(imageGameOver, (half_screen_width - 150, 100))
            self.menu.draw(self.screen, 'Game over. Press any key to restart', half_screen_width, 250)
            self.menu.draw(self.screen, f'Your score: {self.score.count}', half_screen_width, 300)
            self.menu.draw(self.screen, f'Highest score: {self.leader_board.get_highest_score()}', half_screen_width, 350)
            self.menu.draw(self.screen, f'Total deaths: {self.death_count.count}', half_screen_width, 400)
            self.menu.draw(self.screen, f'Press "h" to see the list of highest scores', half_screen_width, 500)

        self.menu.update(self)
        
    def reset(self):
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.score.reset()
        self.heart.reset()
        self.player.reset()
        self.power_up_manager.reset()

    def show_higest_scores(self):
        half_screen_width = SCREEN_WIDTH // 2
        height = 100
        position = 1
    
        self.menu.reset(self.screen)
        
        self.menu.draw(self.screen, 'Highest Scores', half_screen_width, 50)
        for score in self.leader_board.highest_scores:
            self.menu.draw(self.screen, f'{position}: {score}', half_screen_width, height )
            height += 50
            position += 1
        self.menu.draw(self.screen, f'Press "m" to return to the previous menu', half_screen_width, height + 50)
        self.menu.draw(self.screen, f'Press "s" to start a new game', half_screen_width, height + 100)
    
        self.menu.update(self)

        self.save_high_score()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())  / 1000 ,2)

            if time_to_show >= 0:
                self.menu.draw(self.screen, f'{self.player.power_up_type.capitalize()} is enable for {time_to_show} seconds', 520,40, (255,255,0))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()

    def save_high_score(self):
        with open('highest_score.dat', 'wb') as file:
            pickle.dump(self.leader_board.highest_scores, file)

    def load_high_score(self):
        try:
            with open('highest_score.dat', 'rb') as file:
                self.leader_board.highest_scores = pickle.load(file)
        except FileNotFoundError:
            self.leader_board.highest_scores = []