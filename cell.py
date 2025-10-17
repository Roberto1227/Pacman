# Este módulo define la clase Cell, que representa una celda individual dentro del mapa del juego.
# Cada celda tiene una posición absoluta, dimensiones específicas y puede contener una pieza.
# Para facilitar el desarrollo sin depender del renderizado visual, se puede desactivar temporalmente
# el dibujo del rectángulo azul en el método update. Esto permite mantener la lógica de colisiones y
# estructura del mapa sin generar errores gráficos si la superficie de destino no está disponible.

import pygame

class Cell(pygame.sprite.Sprite):
	def __init__(self, row, col, length, width):
		super().__init__()
		self.width = length
		self.height = width
		self.id = (row, col)
		self.abs_x = row * self.width
		self.abs_y = col * self.height

		self.rect = pygame.Rect(self.abs_x,self.abs_y,self.width,self.height)

		self.occupying_piece = None

	def update(self, screen):
		pygame.draw.rect(screen, pygame.Color("blue2"), self.rect)