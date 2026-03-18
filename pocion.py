import pygame
import random

class Pocion:
    def __init__(self, imagen):
        self.image = imagen
        self.rect = self.image.get_rect()
        
        # --- ATRIBUTOS PRIVADOS (Encapsulamiento) ---
        self.__aparecer = False
        self.__tiempo_aparicion = 0
        self.__duracion = 5000  # La poción dura 5 segundos en pantalla

    # --- GETTERS Y SETTERS ---
    @property
    def activa(self):
        return self.__aparecer

    @activa.setter
    def activa(self, valor):
        self.__aparecer = valor

    # --- MÉTODOS DE LÓGICA ---
    def reubicar(self):
        """Coloca la poción en una posición aleatoria y activa su visibilidad"""
        self.rect.x = random.randint(100, 700)
        self.rect.y = random.randint(100, 500)
        self.__aparecer = True
        self.__tiempo_aparicion = pygame.time.get_ticks()

    def actualizar(self):
        """Verifica si el tiempo de la poción ha expirado"""
        if self.__aparecer:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.__tiempo_aparicion > self.__duracion:
                self.__aparecer = False

    def dibujar(self, superficie):
        """Dibuja la poción solo si está activa (Requisito: elementos definidos sin fondo)"""
        if self.__aparecer:
            superficie.blit(self.image, self.rect)