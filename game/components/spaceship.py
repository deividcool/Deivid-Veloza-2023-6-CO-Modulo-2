import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_TYPE
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    X_POS = ( SCREEN_WIDTH // 2 ) - 40
    Y_POS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.has_power_up = False
        self.power_up_timer = 0
        self.power_up_type = DEFAULT_TYPE
        self.guns = 0
        self.speed = 0
        self.lifes = 3


    def update(self, user_input, game):

        if user_input[pygame.K_LEFT]:
            self.move_left(game)
        if  user_input[pygame.K_RIGHT]:
            self.move_right(game)
        if  user_input[pygame.K_UP]:
            self.move_up(game)
        if  user_input[pygame.K_DOWN]:
            self.move_down(game)
        if user_input[pygame.K_SPACE]:
            self.shoot(game)


    def move_left(self,game):
        if self.rect.left > 0:
            self.rect.x -= 10 
        elif self.rect.left < 10:
            self.rect.x = SCREEN_WIDTH - 10 

    def move_right(self,game):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10 
        elif self.rect.right > SCREEN_WIDTH - 10:
            self.rect.x = 10 

    def move_up(self,game):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10 + game.player.speed

    def move_down(self,game):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += 10 + game.player.speed

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def set_image(self, size=(40,60), image=SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
    

    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet)