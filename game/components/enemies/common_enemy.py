from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1


class CommonEnemy(Enemy):
  def __init__(self):
    super().__init__(ENEMY_1)