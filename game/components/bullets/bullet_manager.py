
import pygame
from game.utils.constants import SHIELD_TYPE, GUNENEMY, GUNPLAYER

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
        self.SoundGunEnemy = GUNENEMY
        self.SoundGunPlayer = GUNPLAYER
        self.player_guns = 1
        
    def update(self, game): 

       for bullet in self.enemy_bullets:
        bullet.update(self.enemy_bullets)
      
        if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
            self.enemy_bullets.remove(bullet)
            if game.player.power_up_type != SHIELD_TYPE:
                game.heart.remove_life_image()

                if game.heart.lifes == 0:             
                    game.death_count.update()
                    game.leader_board.update(game.score.count)
                    game.playing = False
                    pygame.time.delay(1000)
                    break

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    enemy.decrease_hitpoints(game)
                    self.player_bullets.remove(bullet)
    

    def draw(self,screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
            
            
        for bullet in self.player_bullets:
            bullet.draw(screen)
           

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy':
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.player_bullets) < (1 + self.player_guns):
            self.player_bullets.append(bullet)

    def reset(self):
        self.enemy_bullets = []
        self.player_bullets = []
    