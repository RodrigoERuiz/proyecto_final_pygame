import pygame

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
FPS = 30
DEBUG = False

SCREEN = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

backgound = pygame.image.load('recursos/backgrounds/41530.jpg').convert_alpha()
backgound = pygame.transform.scale(backgound,(ANCHO_VENTANA,ALTO_VENTANA))