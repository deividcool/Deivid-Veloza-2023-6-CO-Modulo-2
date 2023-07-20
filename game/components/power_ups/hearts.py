import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import ICON

class Hearts(PowerUp):
    def __init__(self):
        self.lifes = 3
        self.lives_images = []
        self.life_image = pygame.transform.scale(ICON, (30, 30))
        for _ in range(self.lifes):
            self.lives_images.append(self.life_image)
    def draw(self, screen):
        x = 20  
        y = 20 
    
        for life_image in self.lives_images:
            screen.blit(life_image, (x, y))
            x += 35
 
    def remove_life_image(self):
        if self.lifes >= 0:
            self.lifes -= 1
            self.lives_images.pop()

    def add_life_image(self):
        self.lifes += 1
        self.lives_images.append(self.life_image)

    def reset(self):
        self.lifes = 3
        self.lives_images = []
        self.life_image = pygame.transform.scale(ICON, (30, 30))
        for _ in range(self.lifes):
            self.lives_images.append(self.life_image)