import pygame
from constantes import *
from auxiliar import SurfaceManager

class Jugador :
    def __init__(self, coord_x, coord_y, velocidad) -> None:
        self.stand_r = [
                        pygame.image.load('recursos/sprites/Stand/0.png'),
                        pygame.image.load('recursos/sprites/Stand/1.png'),
                        pygame.image.load('recursos/sprites/Stand/2.png'),
                        pygame.image.load('recursos/sprites/Stand/3.png'),
                        pygame.image.load('recursos/sprites/Stand/4.png'),
                        pygame.image.load('recursos/sprites/Stand/5.png'),
                        pygame.image.load('recursos/sprites/Stand/6.png'),
                        pygame.image.load('recursos/sprites/Stand/7.png'),
                        pygame.image.load('recursos/sprites/Stand/8.png'),
                        pygame.image.load('recursos/sprites/Stand/9.png')
                    ]
        
        self.walk_r = [
                        pygame.image.load('recursos/sprites/Walk/0.png'),
                        pygame.image.load('recursos/sprites/Walk/1.png'),
                        pygame.image.load('recursos/sprites/Walk/2.png'),
                        pygame.image.load('recursos/sprites/Walk/3.png'),
                        pygame.image.load('recursos/sprites/Walk/4.png'),
                        pygame.image.load('recursos/sprites/Walk/5.png'),
                        pygame.image.load('recursos/sprites/Walk/6.png'),
                        pygame.image.load('recursos/sprites/Walk/7.png'),
                        pygame.image.load('recursos/sprites/Walk/8.png'),
                        pygame.image.load('recursos/sprites/Walk/9.png')
                    ]
        
        self.run_r = [
                        pygame.image.load('recursos/sprites/Run/0.png'),
                        pygame.image.load('recursos/sprites/Run/1.png'),
                        pygame.image.load('recursos/sprites/Run/2.png'),
                        pygame.image.load('recursos/sprites/Run/3.png'),
                        pygame.image.load('recursos/sprites/Run/4.png'),
                        pygame.image.load('recursos/sprites/Run/5.png'),
                        pygame.image.load('recursos/sprites/Run/6.png'),
                        pygame.image.load('recursos/sprites/Run/7.png'),
                        pygame.image.load('recursos/sprites/Run/8.png'),
                        pygame.image.load('recursos/sprites/Run/9.png')
                    ]
       
        #imagenes de animacion escaladas
        self.run_r = SurfaceManager.preparar_imagen(self.run_r,120,120)
        self.run_l = SurfaceManager.girar_sprites(self.run_r)
        self.stand_r = SurfaceManager.preparar_imagen(self.stand_r,120,120)
        self.stand_l = SurfaceManager.girar_sprites(self.stand_r)
        self.walk_r = SurfaceManager.preparar_imagen(self.walk_r, 120,120)
        self.walk_l = SurfaceManager.girar_sprites(self.walk_r)
        

        self.coord_x = coord_x
        self.coord_y = coord_y
        self.velocidad_walk = velocidad
        self.velocidad_run = velocidad * 1.1
        self.frame_actual = 0
        self.animacion_actual = self.stand_r
        self.frame_tiempo_anterior = pygame.time.get_ticks()
        self.frame_tiempo_intervalo = 30  # Intervalo entre cambios de fotograma en milisegundos
        self.is_looking_right = True
        self.is_jump = False
        self.image= self.animacion_actual[self.frame_actual]
        self.velocidad_y = -10
        self.piso = pygame.draw.rect(SCREEN, (255, 0, 0), (0, 521, ANCHO_VENTANA, ALTO_VENTANA))  # Ejemplo de coordenadas y tamaño
        self.height = self.image.get_height() 
        self.width = self.image.get_width()
        self.rectangulo = self.image.get_rect()
        self.esta_cayendo = False
        
    # def aplicar_gravedad(self):
    #     if self.is_jump or self.coord_y < ALTO_VENTANA - self.height: #aca estoy aplicando gravedad cuando el personaje salta o cuando no esta en el piso
    #         #poner la animacion de saltar
    #         self.coord_y -= self.velocidad_y
    #         self.velocidad_y -= 1  
    

    def actualizar(self):
        self.rectangulo.x = self.coord_x
        self.rectangulo.y = self.coord_y
        self.controlar_limites_pantalla()
        if DEBUG:
            pygame.draw.rect(SCREEN, (255, 0, 0), self.rectangulo, 2) 
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.frame_tiempo_anterior > self.frame_tiempo_intervalo:
            self.frame_tiempo_anterior = tiempo_actual
            self.frame_actual = (self.frame_actual + 1) % len(self.stand_r)
            self.image = self.stand_r[self.frame_actual]
            
        if self.is_jump or self.coord_y < ALTO_VENTANA - self.height: #aca estoy aplicando gravedad cuando el personaje salta o cuando no esta en el piso
            #poner la animacion de saltar
            self.coord_y -= self.velocidad_y
            self.velocidad_y -= 1  
            
            #Esto controla que el jugador no se vaya por abajo de la pantalla
            if self.coord_y >= ALTO_VENTANA - self.height:  
                self.coord_y = ALTO_VENTANA - self.height
                self.is_jump = False
                self.velocidad_y = 0

        
    def mover(self, lista_teclas: list):
        if lista_teclas[pygame.K_d] and lista_teclas[pygame.K_LSHIFT]:
            self.animacion_actual = self.run_r
            self.is_looking_right = True
            self.coord_x += self.velocidad_run   
            
          #CORRER A LA IZQUIERDA  
        elif lista_teclas[pygame.K_a] and lista_teclas[pygame.K_LSHIFT]:
            self.animacion_actual = self.run_l
            self.is_looking_right = False
            self.coord_x -= self.velocidad_run   
            #CAMINAR A LA DERECHA
            
        elif lista_teclas[pygame.K_d]:
            self.animacion_actual = self.walk_r
            self.coord_x += self.velocidad_walk
            self.is_looking_right = True
            
            #CAMINAR A LA IZQUIERDA
        elif lista_teclas[pygame.K_a]:
            self.animacion_actual = self.walk_l
            self.coord_x -= self.velocidad_walk
            self.is_looking_right = False
            #QUEDARSE QUIETO
        else:
            if self.is_looking_right:
                self.animacion_actual = self.stand_r
            else:
                self.animacion_actual = self.stand_l
                
            #SALTAR
        if lista_teclas[pygame.K_SPACE] and not self.is_jump:
            self.is_jump = True
            self.velocidad_y = 10 
            
     
    def controlar_limites_pantalla(self):
        if self.rectangulo.right >= ANCHO_VENTANA:
            self.coord_x = ANCHO_VENTANA - self.rectangulo.width
        elif self.rectangulo.left <= 0:
            self.coord_x = 0
        # if self.rectangulo.bottom >= ALTO_VENTANA:
        #     self.coord_y = ALTO_VENTANA - self.rectangulo.height
        #     self.coord_y = 400                      #Sacar el hardcodeo


            #self.rectangulo.bottom = self.piso.top
        # elif self.coord_y <= 0:
        #     self.coord_y = 0
        if DEBUG:
            pygame.draw.rect(SCREEN, (255, 0, 0), (0, 521, ANCHO_VENTANA, ALTO_VENTANA))  # Ejemplo de coordenadas y tamaño
        



#(69, 521) x,y piso