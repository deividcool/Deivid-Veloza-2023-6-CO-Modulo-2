import random

from game.components.enemies.common_enemy import CommonEnemy
from game.components.enemies.enemy_two import StrongEnemy
from game.components.enemies.enemy_three import StrongEnemy3

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, bullet_manager):
        self.add_enemy()
    
        for enemy in self.enemies:
            enemy.update(self.enemies, bullet_manager)
  
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
      
    def add_enemy(self):
        enemy_type = random.randint(1,3)
        if len(self.enemies) < 3:
            if enemy_type == 1:
                enemy = CommonEnemy()
                self.enemies.append(enemy) 
            elif enemy_type == 2:
                enemy = StrongEnemy()
                self.enemies.append(enemy) 
            elif enemy_type == 3:
                enemy = StrongEnemy3()
                self.enemies.append(enemy) 

    def reset(self):
        self.enemies = []