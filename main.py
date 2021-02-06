# Trabalho feito em pygame pelo grupo João Lucas, Arthur Feu, Gustavo Paiva e Caio Augusto

import pygame
import time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('AVENTURA?')

# Variaveis do jogo
tile_size = 50
# Carregando as imagens
bg_img = pygame.image.load('img/bg1.jpg')

clock = pygame.time.Clock()
fps = 60

class Player():
	def __init__(self, x, y):
		self.images_right = []
		self.images_left = []
		self.images_idle = []
		for num in range(1, 2):
			img_idle = pygame.image.load(f'img/breathing{num}.png')
			img_idle = pygame.transform.scale(img_idle, (40, 80))
			self.images_idle.append(img_idle)
		self.index = 0
		self.walkcounter = 0
		self.standcounter = 0
		for num in range(1, 6):
			img_right = pygame.image.load(f'img/walk{num}.png')
			img_right = pygame.transform.scale(img_right, (40, 80))
			img_left = pygame.transform.flip(img_right, True, False)
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.image = self.images_right[3]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0

	def update(self):
		dx = 0
		dy = 0
		walk_cooldown = 5
		stand_cooldown = 2
		# Captura das teclas do usuário
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE] and not self.jumped and not self.in_air:
			self.vel_y = -15
			self.jumped = True
			self.standcounter = 0
		if not key[pygame.K_SPACE]:
			self.jumped = False
			self.standcounter = 0
		if key[pygame.K_LEFT]:
			dx -= 5
			self.walkcounter += 1
			self.direction = -1
			self.standcounter = 0
		if key[pygame.K_RIGHT]:
			dx += 5
			self.walkcounter += 1
			self.direction = 1
			self.standcounter = 0
		if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
			self.walkcounter = 0
			self.index = 0
			self.standcounter += 1
			if self.direction == 1:
				self.image = self.images_right[3]
			if self.direction == -1:
				self.image = self.images_left[3]

		# Animação do personagem
		if self.walkcounter > walk_cooldown:
			self.walkcounter = 0
			self.index += 1
			if self.index >= len(self.images_right):
				self.index = 0
			if self.direction == 1:
				self.image = self.images_right[self.index]
			if self.direction == -1:
				self.image = self.images_left[self.index]
		if self.standcounter > stand_cooldown:
			self.index += 1
			if self.index >= len(self.images_idle):
				self.index = 0
			if self.direction == 1:
				time.sleep(0.02)
				self.image = self.images_idle[self.index]
			if self.direction == -1:
				time.sleep(0.02)
				self.image = pygame.transform.flip(self.images_idle[self.index], True, False)
		# Gravidade
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y

		# Checagem de colisão
		self.in_air = True
		for tile in world.tile_list:
			# Checagem de colisão no eixo x
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				dx = 0
			# Checagem de colisão no eixo y
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				# Pulando
				if self.vel_y < 0:
					dy = tile[1].bottom - self.rect.top
					self.vel_y = 0
				# Caindo
				elif self.vel_y >= 0:
					dy = tile[1].top - self.rect.bottom
					self.vel_y = 0
					self.in_air = False
		# Atualização das coordenadas do jogador
		self.rect.x += dx
		self.rect.y += dy

		if self.rect.bottom > 600:
			self.rect.bottom = 600
		# Desenhar o jogador na tela
		screen.blit(self.image, self.rect)
		# pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

class World():
	def __init__(self, data):
		self.tile_list = []
		# Carregando as imagens de blocos
		dirt_img = pygame.image.load('img/dirt.jpg')
		grass_img = pygame.image.load('img/grass.jpg')
		platform_img = pygame.image.load('img/platform.jpg')
		platformwograss_img = pygame.image.load('img/platform2.jpg')
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					img = pygame.transform.scale(platform_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 4:
					img = pygame.transform.scale(platformwograss_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])
			# pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 2, 2],
[1, 7, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 2, 2, 1, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1],
]

player = Player(100, 600 - 130)
world = World(world_data)

run = True
while run:

	clock.tick(fps)

	screen.blit(bg_img, (0, 0))

	world.draw()

	player.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()