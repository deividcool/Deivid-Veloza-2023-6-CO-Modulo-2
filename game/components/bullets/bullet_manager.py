
import pygame
from game.utils.constants import SHIELD_TYPE, GUNENEMY, GUNPLAYER

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.player_bullets = []
        self.SoundGunEnemy = GUNENEMY
        self.SoundGunPlayer = GUNPLAYER
        self.player_guns = 0


    def update(self, game):
        self.player_guns = game.player.guns 

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                game.remove_life_image()
                self.enemy_bullets.remove(bullet)   

                if game.lifes == 0:
                    game.playing = False
                    pygame.time.delay(1000)
                    game.update_death_count()
            
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner != 'enemy':
                    self.player_bullets.remove(bullet)
                    game.enemy_manager.enemies.remove(enemy)
                    game.update_score()
            break        

    def draw(self,screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
            
            
        for bullet in self.player_bullets:
            bullet.draw(screen)
           

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        if bullet.owner == 'player' and len(self.player_bullets) <= self.player_guns:
            self.player_bullets.append(bullet)
    