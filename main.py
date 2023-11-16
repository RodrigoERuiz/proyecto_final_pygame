from constantes import *
from jugador import Jugador
import pygame

pygame.init()
reloj = pygame.time.Clock()

its_running = True

jugador = Jugador(70,400,5)

while its_running:
    reloj.tick(FPS)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            its_running = False
            break
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento)
    
    SCREEN.blit(backgound,(0,0))
    
    
    teclas_presionadas = pygame.key.get_pressed()
    jugador.mover(teclas_presionadas)
    jugador.actualizar()
    
    pygame.display.update()



pygame.quit()