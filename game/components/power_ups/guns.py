from game.components.power_ups.power_up import PowerUp
from game.utils.constants import GUN, BULLET_TYPE

class Guns(PowerUp):
    def __init__(self):
        super().__init__(GUN, BULLET_TYPE)