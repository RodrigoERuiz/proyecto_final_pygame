import pygame
from auxiliar import SurfaceManager
from constantes import *
from jugador import Jugador


class Enemigo():
    def __init__(self, coord_x, coord_y, velocidad):
        # self.stand_r = SurfaceManager.get_surface_from_spritesheet('recursos/enemies/Mask Dude/Idle (32x32).png',11,1,1,False)
        # self.stand_l = SurfaceManager.get_surface_from_spritesheet('recursos/enemies/Mask Dude/Idle (32x32).png',11,1,1,True)
        # self.walk_r =  SurfaceManager.get_surface_from_spritesheet('recursos/enemies/Mask Dude/Run (32x32).png',11,1,1,False)
        # self.walk_l = SurfaceManager.get_surface_from_spritesheet('recursos/enemies/Mask Dude/Run (32x32).png',11,1,1,True)

        # #lista de imagenes escaldas
        # self.stand_r = SurfaceManager.preparar_imagen(self.stand_r,80,80)
        # self.stand_l = SurfaceManager.preparar_imagen(self.stand_l,80,80)
        # self.walk_r = SurfaceManager.preparar_imagen(self.walk_r,80,80)
        # self.walk_l = SurfaceManager.preparar_imagen(self.walk_l,80,80)
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
        self.frame_actual = 0
        self.animacion_actual = self.stand_l
        self.image = self.animacion_actual[self.frame_actual]
        self.rectangulo = self.image.get_rect()
        self.velocidad  = velocidad
        self.height = self.image.get_height() 
        self.width = self.image.get_width()
        self.direccion = 1  # 1 para derecha, -1 para izquierda
        self.velocidad_y = -1
        self.frame_tiempo_anterior = pygame.time.get_ticks()
        self.frame_tiempo_intervalo = 30
        
    
    def aplicar_gravedad(self):
        if self.coord_y < ALTO_VENTANA - self.height: #aca estoy aplicando gravedad cuando el personaje salta o cuando no esta en el piso
            self.coord_y -= self.velocidad_y
            self.velocidad_y -= 1  
            
            #Esto controla que el jugador no se vaya por abajo de la pantalla ARREGLAR INTEGRAR A COTROLAR_LIMITES_PANTALLA
            if self.coord_y >= ALTO_VENTANA - self.height:  
                self.coord_y = ALTO_VENTANA - self.height
                self.velocidad_y = 0
    
    
    
    def controlar_limites_pantalla(self):
        if self.rectangulo.right >= ANCHO_VENTANA:
            self.coord_x = ANCHO_VENTANA - self.rectangulo.width
        elif self.rectangulo.left <= 0:
            self.coord_x = 0
            
                
    def mover(self):
        self.animar()
        if self.rectangulo.right >= ANCHO_VENTANA:
            self.direccion = -1  # Cambiar a la izquierda si alcanza el borde derecho
            self.animacion_actual = self.walk_l
        elif self.rectangulo.left <= 0:
            self.direccion = 1   # Cambiar a la derecha si alcanza el borde izquierdo
            self.animacion_actual = self.walk_r
        # Mover en la dirección correspondiente
        self.rectangulo.x += self.velocidad * self.direccion
        
        
    def animar(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.frame_tiempo_anterior > self.frame_tiempo_intervalo:
            self.frame_tiempo_anterior = tiempo_actual
            self.frame_actual = (self.frame_actual + 1) % len(self.stand_r)
            self.image = self.stand_r[self.frame_actual]
                
        # Aplicar gravedad
        self.aplicar_gravedad()
        
        # Actualizar las coordenadas del rectángulo en y
        self.rectangulo.y = self.coord_y

            
    def actualizar(self):
        self.controlar_limites_pantalla()
        self.mover()
        
        
    
        