# Trabalho feito em pygame pelo grupo João Lucas, Arthur Feu, Gustavo Paiva e Caio Augusto

import pygame
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Jornada por Gavendish')

# Fontes e cores
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30)
white = (255, 255, 255)
blue = (0, 0, 255)

# Variáveis de auxílio
tile_size = 50
gameOver = 0
level = 1
maxLevels = 2
totalScore = 0
scoreInLevel = 0
keyCollected = 0
clock = pygame.time.Clock()
fps = 60


def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


# Carregando as imagens
bg_img = pygame.image.load('img/bg1.png')
restart_img = pygame.image.load('img/restart_btn.png')
exit_img = pygame.image.load('img/exit_btn.png')
exit_img = pygame.transform.scale(exit_img, (120, 42))

# Função que reseta o nível


def reset_level(level):
	player.__init__(100, 600 - 130)
	enemy_group.empty()
	lava_group.empty()
	exit_group.empty()

	# load in level data and create world
	archive = open(f'level{level}.txt', 'r')
	data = archive.read()
	archive.close()
	data = data.split('\n')
	world_data = []
	for num in range(0, 12):
		world_data.append(list(data[num]))

	world = World(world_data)
	return world
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
		self.imagesIdle = []
		for num in range(1, 6):
			imgRight = pygame.image.load(f'img/walk{num}.png')
			imgRight = pygame.transform.scale(imgRight, (40, 80))
			imgLeft = pygame.transform.flip(imgRight, True, False)
			self.imagesRight.append(imgRight)
			self.imagesLeft.append(imgLeft)
		for num in range(1, 7):
			imgDead = pygame.image.load(f'img/death{num}.png')
			imgDead = pygame.transform.scale(imgDead, (40, 80))
			self.imagesDead.append(imgDead)
		for num in range(1, 2):
			imgIdle = pygame.image.load(f'img/idle{num}.png')
			imgIdle = pygame.transform.scale(imgIdle, (40, 80))
			self.imagesIdle.append(imgIdle)
		self.image = self.imagesIdle[0]
		self.rect = self.image.get_rect()
		self.index = 0
		self.walkCounter = 0
		self.standCounter = 0
		self.lastUpdate = 0
		self.currentFrame = 0
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.walked = False
		self.direction = 0
		self.inAir = True

	def update(self, gameOver):
		dx = 0
		dy = 0
		walk_cooldown = 5

		if gameOver == 0:
			#self.idle()
			# Captura das teclas do usuário
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE] and not self.jumped and not self.inAir:
				self.vel_y = -15
				self.jumped = True
				self.standCounter = 0
			if not key[pygame.K_SPACE]:
				self.jumped = False
				self.standCounter = 0
			if key[pygame.K_LEFT]:
				dx -= 5
				self.walked = True
				self.walkCounter += 1
				self.direction = -1
				self.standCounter = 0
			if key[pygame.K_RIGHT]:
				dx += 5
				self.walked = True
				self.walkCounter += 1
				self.direction = 1
				self.standCounter = 0
			if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
				self.walkCounter = 0
				self.index = 0
				self.standCounter += 1
				if self.direction == 1:
					self.image = self.imagesRight[3]
				if self.direction == -1:
					self.image = self.imagesLeft[3]

			# Animação do personagem

			# Andando
			if self.walkCounter > walk_cooldown:
				self.walkCounter = 0
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
			self.inAir = True
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
						self.inAir = False

			# Checagem de colisão com os inimigos
			if pygame.sprite.spritecollide(self, enemy_group, False):
				gameOver = -1

			# Checagem de colisão com a lava
			if pygame.sprite.spritecollide(self, lava_group, False):
				gameOver = -1

			# Checagem de colisão com a porta de saída
			if keyCollected == 1:
				if pygame.sprite.spritecollide(self, exit_group, False):
					gameOver = 1

			# Atualização das coordenadas do jogador
			self.rect.x += dx
			self.rect.y += dy

		elif gameOver == -1:
			draw_text('GAME OVER!', font, white, (900 // 2) - 150, 0)
			self.standCounter += 1
			self.image = self.imagesDead[self.index]
			if self.standCounter > 7:
				if self.index >= (len(self.imagesDead) - 1):
					return gameOver
				else:
					self.index += 1
				self.standCounter = 0

		# Desenhar o jogador na tela
		screen.blit(self.image, self.rect)
		# pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

		return gameOver

	def idle(self):
		# Animação de idle do usuário
		now = pygame.time.get_ticks()
		if not self.jumped and not self.walked:
			if now - self.lastUpdate > 350:
				self.lastUpdate = now
				self.currentFrame = (self.currentFrame + 1) % len(self.imagesIdle)
				bottom = self.rect.bottom
				self.image = self.imagesIdle[self.currentFrame]
				self.rect = self.image.get_rect()
				self.rect.bottom = bottom
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
				if tile == '1':
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == '2':
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == '3':
					img = pygame.transform.scale(platform_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == '4':
					img = pygame.transform.scale(platformwograss_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == '5':
					enemy = Enemy(col_count * tile_size, row_count * tile_size + 12)
					enemy_group.add(enemy)
				if tile == '6':
					lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
					lava_group.add(lava)
				if tile == '7':
					coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
					coin_group.add(coin)
				if tile == '8':
					exitdoor = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
					exit_group.add(exitdoor)
				if tile == '9':
					key = Key(col_count * tile_size, row_count * tile_size - (tile_size // 2))
					key_group.add(key)
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
		self.imagesRight = []
		self.imagesLeft = []
		for num in range(1, 4):
			imgWalk = pygame.image.load(f'img/enemy{num}.png')
			self.imagesRight.append(imgWalk)
			img_left = pygame.transform.flip(imgWalk, True, False)
			self.imagesLeft.append(img_left)
		self.image = self.imagesRight[0]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.moveDirection = 1
		self.moveCounter = 0
		self.spriteChanger = 0
		self.index = 0

	def update(self):
		self.rect.x += self.moveDirection
		self.moveCounter += 1
		self.spriteChanger += 1
		walkCooldown = 25
		if self.spriteChanger > walkCooldown:
			self.spriteChanger = 0
			self.index += 1
			if self.index >= len(self.imagesRight):
				self.index = 0
			if self.moveDirection == -1:
				self.image = self.imagesRight[self.index]
			if self.moveDirection == 1:
				self.image = self.imagesLeft[self.index]
		if abs(self.moveCounter) > 50:
			self.moveDirection *= -1
			self.moveCounter *= -1

# Classe da lava, obstáculo do jogo


class Lava(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/lava.png')
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

# Classe da moeda do jogo


class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/coin.png')
		self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

# Classe da chave do jogo


class Key(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/key.png')
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

# Classe da porta de saida do nível


class Exit(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/exitlocked.png')
		self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.isLocked = True

	def update(self):
		if keyCollected == 0:
			img = pygame.image.load('img/exitlocked.png')
			self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
		if keyCollected == 1:
			img = pygame.image.load('img/exit.png')
			self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))


# Carregando o mapa do jogo

archive = open(f'level{level}.txt', 'r')
data = archive.read()
archive.close()
data = data.split('\n')
world_data = []
for num in range(0, 12):
	world_data.append(list(data[num]))

player = Player(100, 600 - 130)

enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
key_group = pygame.sprite.Group()
vanity_coin = pygame.sprite.Group()
vanity_key = pygame.sprite.Group()

score_coin = Coin(tile_size // 2 - 3, tile_size // 2 - 8)
score_key = Key(tile_size + 60, tile_size // 2 - 5)
vanity_coin.add(score_coin)
vanity_key.add(score_key)

world = World(world_data)

# Criação dos botões
restart_button = Button(900 // 2 - 50, 600 // 2, restart_img)
exit_button = Button(900 // 2 + 50, 600 // 2, exit_img)

# Loop do jogo
run = True
while run:
	clock.tick(fps)
	screen.blit(bg_img, (0, 0))
	world.draw()

	# Enquanto o jogador estiver no jogo
	if gameOver == 0:
		enemy_group.update()
		# Atualização do placar, com checagem se a moeda foi coletada pelo jogador
		if pygame.sprite.spritecollide(player, coin_group, True):
			totalScore += 1
			scoreInLevel += 1
		if pygame.sprite.spritecollide(player, key_group, True):
			keyCollected = 1
			exit_group.update()
		draw_text('X ' + str(totalScore), font_score, white, tile_size - 10, 10)
		draw_text('X ' + str(keyCollected), font_score, white, tile_size + 90, 10)
	if gameOver == 0:
		enemy_group.update()

	enemy_group.draw(screen)
	lava_group.draw(screen)
	coin_group.draw(screen)
	exit_group.draw(screen)
	key_group.draw(screen)
	vanity_key.draw(screen)
	vanity_coin.draw(screen)

	gameOver = player.update(gameOver)

	# Caso o jogador morra
	if gameOver == -1:
		if restart_button.draw():
			world_data = []
			world = reset_level(level)
			gameOver = 0
			keyCollected = 0
			totalScore -= scoreInLevel

	# Caso o jogador ganhe
	if gameOver == 1:
		# Reset do jogo e ida ao proximo nivel
		level += 1
		scoreInLevel = 0
		coin_group.remove(coin_group)
		key_group.remove(key_group)
		# Caso ainda tenha mais níveis
		if level <= maxLevels:
			# Reset do nível
			world_data = []
			world = reset_level(level)
			gameOver = 0
			keyCollected = 0
		# Caso seja o último
		else:
			draw_text('YOU WIN!', font, blue, (900 // 2) - 100, 0)
			if restart_button.draw():
				# Reset do nível
				level = 1
				world_data = []
				world = reset_level(level)
				gameOver = 0
				keyCollected = 0
				totalScore = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
