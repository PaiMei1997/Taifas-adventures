import pygame
import random

# --- CLASE BASE (Herencia) ---
class Raton:
    def __init__(self, imagenes):
        # Usamos un solo guion bajo para indicar que son protegidos (Encapsulamiento)
        self._image = random.choice(imagenes)
        self.rect = self._image.get_rect()
        self.rect.x = random.choice([-50, 850])
        self.rect.y = random.randint(50, 550)
        self._velocidad = random.randint(3, 6)
        self._dir = 1 if self.rect.x < 0 else -1
        
    def mover(self): 
        """Movimiento básico lineal"""
        self.rect.x += self._velocidad * self._dir
        
    def dibujar(self, superficie): 
        superficie.blit(self._image, self.rect)

# --- CLASE HIJA (Herencia y Polimorfismo) ---
class RatonJefe(Raton): # Hereda de Raton [cite: 39]
    def __init__(self, imagen):
        # Llamamos al constructor del padre pero personalizamos la imagen y posición
        super().__init__([imagen]) 
        self.rect = self._image.get_rect(center=(-100, 300))
        self._velocidad = 1.5

    # Sobrescribimos el método mover (Polimorfismo) 
    def mover(self, objetivo_rect=None):
        """Moverse persiguiendo al jugador en lugar de ir en línea recta"""
        if objetivo_rect:
            if self.rect.x < objetivo_rect.x: self.rect.x += self._velocidad
            if self.rect.x > objetivo_rect.x: self.rect.x -= self._velocidad
            if self.rect.y < objetivo_rect.y: self.rect.y += self._velocidad
            if self.rect.y > objetivo_rect.y: self.rect.y -= self._velocidad
        else:
            # Si no hay objetivo, usa el movimiento normal del padre
            super().mover()