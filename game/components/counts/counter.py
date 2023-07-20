import pygame

from game.utils.constants import FONT_STYLE


class Counter:
  def __init__(self):
    self.count = 0

  def update(self):
    self.count += 1

  def draw(self, screen, message, center):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(f'{message}: {self.count}', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = center
    screen.blit(text, text_rect)

  def reset(self):
    self.count = 0
