# Trabalho feito em pygame pelo grupo João Lucas, Arthur Feu, Gustavo Paiva e Caio Augusto

import pygame

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('AVENTURA?')

# Variaveis do jogo
tile_size = 50
game_over = 0

# Carregando as imagens
bg_img = pygame.image.load('img/bg1.jpg')
restart_img = pygame.image.load('img/restart_btn.png')

clock = pygame.time.Clock()
fps = 60

# Classe dos botões


class Button:
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		# Posição do mouse
		pos = pygame.mouse.get_pos()

		# Checar se o mouse está em cima do botão, clicando
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		# Desenho do botão
		screen.blit(self.image, self.rect)

		return action

# Classe do jogador


class Player:
	def __init__(self, x, y):
		self.imagesRight = []
		self.imagesLeft = []
		self.imagesDead = []
		for num in range(1, 6):
			img_right = pygame.image.load(f'img/walk{num}.png')
			img_right = pygame.transform.scale(img_right, (40, 80))
			img_left = pygame.transform.flip(img_right, True, False)
			self.imagesRight.append(img_right)
			self.imagesLeft.append(img_left)
		for num in range(1, 7):
			img_dead = pygame.image.load(f'img/death{num}.png')
			img_dead = pygame.transform.scale(img_dead, (40, 80))
			self.imagesDead.append(img_dead)
		self.image = self.imagesRight[3]
		self.rect = self.image.get_rect()
		self.index = 0
		self.walkcounter = 0
		self.standcounter = 0
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0
		self.in_air = True

	def update(self, gameOver):
		dx = 0
		dy = 0
		walk_cooldown = 5

		if gameOver == 0:
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
					self.image = self.imagesRight[3]
				if self.direction == -1:
					self.image = self.imagesLeft[3]

			# Animação do personagem
			if self.walkcounter > walk_cooldown:
				self.walkcounter = 0
				self.index += 1
				if self.index >= len(self.imagesRight):
					self.index = 0
				if self.direction == 1:
					self.image = self.imagesRight[self.index]
				if self.direction == -1:
					self.image = self.imagesLeft[self.index]
			# Gravidade
			self.vel_y += 1
			if self.vel_y > 10:
				self.vel_y = 10
			dy += self.vel_y

			# Checagem de colisão com os blocos
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

			# Checagem de colisão com os inimigos
			if pygame.sprite.spritecollide(self, blob_group, False):
				gameOver = -1

			# Checagem de colisão com a lava
			if pygame.sprite.spritecollide(self, lava_group, False):
				gameOver = -1

			# Atualização das coordenadas do jogador
			self.rect.x += dx
			self.rect.y += dy

		elif gameOver == -1:
			self.standcounter += 1
			self.image = self.imagesDead[self.index]
			if self.standcounter > 7:
				if self.index >= (len(self.imagesDead) - 1):
					return gameOver
				else:
					self.index += 1
				self.standcounter = 0

		# Desenhar o jogador na tela
		screen.blit(self.image, self.rect)
		# pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

		return gameOver

# Classe do mundo


class World:
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
				if tile == 5:
					blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
					blob_group.add(blob)
				if tile == 6:
					lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
					lava_group.add(lava)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])
			# pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

# Classe do inimigo


class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/blob.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0

	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 50:
			self.move_direction *= -1
			self.move_counter *= -1

# Classe da lava, obstáculo do jogo


class Lava(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/lava.png')
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


world_data = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 2, 2],
	[1, 7, 0, 0, 0, 0, 0, 5, 0, 0, 0, 3, 3, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 4, 3, 0, 0, 0, 1],
	[1, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 2, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 2, 2, 1, 1],
	[1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1],
	[1, 0, 0, 0, 0, 2, 1, 1, 1, 6, 6, 6, 6, 6, 1, 1, 1, 1],
	[1, 2, 2, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 1, 1, 1, 1],
]

player = Player(100, 600 - 130)

blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()

world = World(world_data)

# Criação dos botões
restart_button = Button(900 // 2 - 50, 600 // 2, restart_img)

run = True
while run:

	clock.tick(fps)
	screen.blit(bg_img, (0, 0))
	world.draw()

	if game_over == 0:
		blob_group.update()

	blob_group.draw(screen)
	lava_group.draw(screen)

	game_over = player.update(game_over)

	# Caso o jogador morra
	if game_over == -1:
		if restart_button.draw():
			player.__init__(100, 600 - 130)
			game_over = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
