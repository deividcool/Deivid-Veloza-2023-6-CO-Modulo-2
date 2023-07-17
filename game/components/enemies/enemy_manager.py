from game.components.enemies.enemy import Enemy
from game.components.enemies.enemytwo import EnemyTwo
from game.components.enemies.enemythree import EnemyThree

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemies2 = []
        self.enemies3 = []
    
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
        for enemy in self.enemies2:
            enemy.update(self.enemies2, game)
        for enemy in self.enemies3:
            enemy.update(self.enemies3, game)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy = Enemy()
            self.enemies.append(enemy)
        if len(self.enemies2) < 1:
            enemytwo = EnemyTwo()
            self.enemies2.append(enemytwo)
        if len(self.enemies3) < 1:
            enemyThree = EnemyThree()
            self.enemies3.append(enemyThree)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        for enemytwo in self.enemies2:
            enemytwo.draw(screen)
        for enemyThree in self.enemies3:
            enemyThree.draw(screen)

    def reset(self):
        self.enemies = []
        self.enemies2 = []
        self.enemies3 = []