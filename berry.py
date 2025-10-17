# Este módulo define la clase Berry, que representa los objetos recolectables en el juego.
# Cada instancia puede ser un punto normal o un potenciador, y se dibuja como un círculo en pantalla.
# Para evitar errores gráficos durante el desarrollo, se puede comentar la línea de dibujo en el método update
# si no se desea renderizar visualmente o si hay problemas con la superficie de destino.
# Esta clase sigue siendo funcional para pruebas de colisiones y lógica de juego, incluso sin renderizado.

import pygame

from settings import CHAR_SIZE, PLAYER_SPEED

class Berry(pygame.sprite.Sprite):
	def __init__(self, row, col, size, is_power_up = False):
		super().__init__()
		self.power_up = is_power_up
		self.size = size
		self.color = pygame.Color("gold") if is_power_up else pygame.Color("white")
		self.thickness = size
		self.abs_x = (row * CHAR_SIZE) + (CHAR_SIZE // 2)
		self.abs_y = (col * CHAR_SIZE) + (CHAR_SIZE // 2)

		# temporary rect for colliderect-checking
		self.rect = pygame.Rect(self.abs_x,self.abs_y, self.size * 2, self.size * 2)

	def update(self, screen):
		self.rect = pygame.draw.circle(screen, self.color, (self.abs_x, self.abs_y), self.size, self.thickness)
		
