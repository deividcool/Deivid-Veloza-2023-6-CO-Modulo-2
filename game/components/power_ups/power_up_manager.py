import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.guns import Guns
from game.components.power_ups.heart import Heart
from game.utils.constants import SPACESHIP_SHIELD


class PowerUpManager:
    POWER_UP_INITIAL_TIME = 6000
    POWER_UP_FINAL_TIME = 8000

    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(self.POWER_UP_INITIAL_TIME, self.POWER_UP_FINAL_TIME)
        self.duration = random.randint(3,5)
    
    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):

                game.player.power_up_type = power_up.type
                if power_up.type == 'shield':
                    game.player.has_power_up = True
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.set_image((65,75),SPACESHIP_SHIELD)
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    self.power_ups.remove(power_up)
                if power_up.type == 'bullet':
                    game.bullet_manager.player_guns += 2    
                    self.power_ups.remove(power_up)
                if power_up.type == 'heart':
                    game.heart.add_life_image()
                    self.power_ups.remove(power_up)
                


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        
    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + self.POWER_UP_INITIAL_TIME, now + self.POWER_UP_FINAL_TIME)

    def generate_power_up(self):
        power_up_type = random.randint(1,3)
        if power_up_type == 1:
            power_up = Shield()
            self.power_ups.append(power_up)
            self.when_appears += random.randint(self.POWER_UP_INITIAL_TIME, self.POWER_UP_FINAL_TIME)
        elif power_up_type == 2:
            power_up = Guns()
            self.power_ups.append(power_up)
            self.when_appears += random.randint(self.POWER_UP_INITIAL_TIME, self.POWER_UP_FINAL_TIME)
        elif power_up_type == 3:
            power_up = Heart()
            self.power_ups.append(power_up)
            self.when_appears += random.randint(self.POWER_UP_INITIAL_TIME, self.POWER_UP_FINAL_TIME)

