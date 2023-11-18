import pygame
from constantes import *

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        
        self.image = pygame.transform.scale(PLATAFORMA_IMAGE,(width,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    