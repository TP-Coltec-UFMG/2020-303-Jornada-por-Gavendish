# Trabalho feito em pygame pelo grupo João Lucas, Arthur Feu, Gustavo Paiva e Caio Augusto

import pygame
from jogador import Player
from mundo import World
from chave import Key
from moeda import Coin

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

world = World(world_data, enemy_group, lava_group, coin_group, exit_group, key_group)

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
			exit_group.update(keyCollected)
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

	gameOver = player.update(gameOver, world, enemy_group, lava_group, exit_group, keyCollected, vanity_coin, vanity_key)

	# Caso o jogador morra
	if gameOver == -1:
		if restart_button.draw():
			world_data = []
			world = World.reset_level(level, player, enemy_group, lava_group, exit_group, coin_group, key_group)
			gameOver = 0
			keyCollected = 0
			totalScore -= scoreInLevel
			scoreInLevel = 0
			score_coin = Coin(tile_size // 2 - 3, tile_size // 2 - 8)
			score_key = Key(tile_size + 60, tile_size // 2 - 5)
			vanity_coin.add(score_coin)
			vanity_key.add(score_key)

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
			world = World.reset_level(level, player, enemy_group, lava_group, exit_group, coin_group, key_group)
			gameOver = 0
			keyCollected = 0
			score_coin = Coin(tile_size // 2 - 3, tile_size // 2 - 8)
			score_key = Key(tile_size + 60, tile_size // 2 - 5)
			vanity_coin.add(score_coin)
			vanity_key.add(score_key)
		# Caso seja o último
		else:
			draw_text('YOU WIN!', font, blue, (900 // 2) - 100, 0)
			if restart_button.draw():
				# Reset do nível
				level = 1
				world_data = []
				world = World.reset_level(level, player, enemy_group, lava_group, exit_group, coin_group, key_group)
				gameOver = 0
				keyCollected = 0
				totalScore = 0
				score_coin = Coin(tile_size // 2 - 3, tile_size // 2 - 8)
				score_key = Key(tile_size + 60, tile_size // 2 - 5)
				vanity_coin.add(score_coin)
				vanity_key.add(score_key)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
