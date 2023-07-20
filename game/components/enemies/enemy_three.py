import random

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3


class StrongEnemy3(Enemy):
    SPEED_X = 10
    SPEED_Y = 1
    INITIAL_SHOOTING_TIME = 1000
    FINAL_SHOOTING_TIME = 2000

    def __init__(self):
        move_x_for = random.randint(10, 80)
        super().__init__(ENEMY_3, self.SPEED_X, self.SPEED_Y, move_x_for)
        self.move_y_for = random.randint(0, 80)
        self.index_y = 0
        self.hitpoints = 3
    
    def change_movement_x(self):
        super().change_movement_x()
        self.index_y += 1
        if self.index_y >= self.move_y_for:
            self.speed_y = 0 if self.speed_y > 0 else self.SPEED_Y
            self.move_y_for = random.randint(50, 100) if self.speed_y == 0 else random.randint(10, 50)
            self.index_y = 0