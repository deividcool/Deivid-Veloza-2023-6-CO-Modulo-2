import pygame
import os

pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
SPEED = pygame.image.load(os.path.join(IMG_DIR, 'Other/Ghost.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
BULLET_TYPE = 'bullet'
SPEED_TYPE = 'bullet'
HEART_TYPE = 'heart'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_boss.gif"))

FONT_STYLE = 'freesansbold.ttf'

INTRO = pygame.mixer.Sound(os.path.join(IMG_DIR,"Sounds/intro.mp3"))
INTRO.set_volume(0.2)
COMBAT = pygame.mixer.Sound(os.path.join(IMG_DIR,"Sounds/soundcombat.mp3"))
GUNENEMY = pygame.mixer.Sound(os.path.join(IMG_DIR,"Sounds/GunEnemy.mp3"))
GUNPLAYER = pygame.mixer.Sound(os.path.join(IMG_DIR,"Sounds/GunPlayer.mp3"))
