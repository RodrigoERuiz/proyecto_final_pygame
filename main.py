from constantes import *
from jugador import Jugador
from enemigo import Enemigo
from plataforma import Plataforma
import pygame

pygame.init()
reloj = pygame.time.Clock()

its_running = True

jugador = Jugador(70,0,5)
enemigos = Enemigo.crear_lista_de_enemigos(5,120)
grupo_enemigos = pygame.sprite.Group()
grupo_enemigos.add(enemigos)

plataforma = Plataforma(255,500,100)
plataformas = pygame.sprite.Group()
plataformas.add(plataforma)

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
    SCREEN.blit(plataforma.image,plataforma.rect)
    
    #Jugador
    jugador.mover(teclas_presionadas)
    jugador.actualizar(plataforma)
    SCREEN.blit(pygame.transform.scale(jugador.animacion_actual[jugador.frame_actual],(jugador.height,jugador.width)), jugador.rect)
    
    
    #plataforma
    if plataforma.rect.colliderect(jugador.rect): #sacar esto de acá
        if plataforma.rect.top <= jugador.rect.bottom:
            jugador.velocidad_y = 0
            jugador.is_jump = False

    
    #Enemigos
    for enemigo in grupo_enemigos:
        enemigo.actualizar()
        jugador.hubo_colision(enemigo.rect)
            
        SCREEN.blit(pygame.transform.scale(enemigo.animacion_actual[enemigo.frame_actual],(enemigo.height,enemigo.width)), enemigo.rect)


    
    pygame.display.update()



pygame.quit()