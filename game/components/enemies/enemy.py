import pygame
import random

from pygame.sprite import Sprite

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet


class Enemy(Sprite):
  ENEMY_WIDTH = 40
  ENEMY_HEIGHT = 60
  
  Y_POS = 20
  
  SPEED_X = 5
  SPEED_Y = 1
  
  MOV_X = { 0: 'left', 1: 'right' }
  
  INITIAL_SHOOTING_TIME = 3000
  FINAL_SHOOTING_TIME = 6000
  
  def __init__(self, image, speed_x = SPEED_X, speed_y = SPEED_Y, move_x_for = random.randint(30, 100)):
    self.image = pygame.transform.scale(image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
    self.rect = self.image.get_rect()
    self.rect.x = random.randrange(self.ENEMY_WIDTH, SCREEN_WIDTH - self.ENEMY_WIDTH, self.ENEMY_WIDTH)
    self.rect.y = self.Y_POS
    self.speed_x = speed_x
    self.speed_y = speed_y
    self.movement_x = self.MOV_X[random.randint(0, 1)]
    self.move_x_for = move_x_for
    self.index = 0
    self.type = 'enemy'
    current_time = pygame.time.get_ticks()
    self.shooting_time = random.randint(current_time + self.INITIAL_SHOOTING_TIME, current_time + self.FINAL_SHOOTING_TIME)
    self.hitpoints = 1
    
  
  def update(self, ships, bullet_manager):
    self.rect.y += self.speed_y
    self.shoot(bullet_manager)
    
    if self.movement_x == 'left':
      self.rect.x -= self.speed_x
      self.change_movement_x()
    else:
      self.rect.x += self.speed_x
      self.change_movement_x()
    
    if self.rect.y >= SCREEN_HEIGHT:
      ships.remove(self)
  
  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
    
  def change_movement_x(self):
    self.index += 1
    if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
      self.movement_x = 'left'
      self.index = 0
    elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= self.ENEMY_WIDTH):
      self.movement_x = 'right'
      self.index = 0
      
  def shoot(self, bullet_manager):
    current_time = pygame.time.get_ticks()
    if self.shooting_time <= current_time:
      bullet = Bullet(self)
      bullet_manager.add_bullet(bullet)
      self.shooting_time += random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)
      
      
  def decrease_hitpoints(self, game):
    self.hitpoints -= 1
    if self.hitpoints <= 0:
      game.score.update()
      game.enemy_manager.enemies.remove(self)
