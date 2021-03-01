# Trabalho feito em pygame pelo grupo Joao Lucas, Arthur Feu, Gustavo Paiva e Caio Augusto

import pygame
from jogador import Player
from mundo import World
from chave import Key
from moeda import Coin

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Jornada por Gavendish')

# Fontes e cores
font = "Retro.ttf"
white = (255, 255, 255)
black = (0, 0, 0)


def text_format(message, textFont, textSize, textColor):
	newFont = pygame.font.Font(textFont, textSize)
	newText = newFont.render(message, False, textColor)
	return newText

# Classe dos botões


class Button:
	def __init__(self, x, y, image):
		self.image = image
		self.image = pygame.transform.scale(self.image, (200, 50))
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


class Main:
	def __init__(self, daltonism):
		# Variáveis de auxílio
		self.tile_size = 50
		self.gameOver = 0
		self.level = 1
		self.maxLevels = 4
		self.totalScore = 0
		self.scoreInLevel = 0
		self.keyCollected = 0
		clock = pygame.time.Clock()
		self.fps = 60
		self.daltonism = daltonism

		# Carregando as imagens
		bgImg = pygame.image.load(f'assets/img/{self.daltonism}/bg1.png')
		restartImg = pygame.image.load(f'assets/img/{self.daltonism}/restart_btn.jpg')

		# Carregando o mapa do jogo
		archive = open(f'assets/levels/level{self.level}.txt', 'r')
		data = archive.read()
		archive.close()
		data = data.split('\n')
		world_data = []
		for num in range(0, 12):
			world_data.append(list(data[num]))

		player = Player(50, 600 - 130, self.daltonism)

		enemyGroup = pygame.sprite.Group()
		lavaGroup = pygame.sprite.Group()
		coinGroup = pygame.sprite.Group()
		exitGroup = pygame.sprite.Group()
		keyGroup = pygame.sprite.Group()

		vanityCoin = pygame.sprite.Group()
		vanityKey = pygame.sprite.Group()
		scoreCoin = Coin(self.tile_size // 2 - 3, self.tile_size // 2 - 8, self.daltonism)
		scoreKey = Key(self.tile_size + 60, self.tile_size // 2 - 5, self.daltonism)
		vanityCoin.add(scoreCoin)
		vanityKey.add(scoreKey)

		world = World(world_data, enemyGroup, lavaGroup, coinGroup, exitGroup, keyGroup, self.daltonism)

		# Criação dos botões
		restartButton = Button(900 // 2 - 100, 600 // 2, restartImg)

		# Loop do jogo
		run = True
		while run:
			clock.tick(self.fps)
			screen.blit(bgImg, (0, 0))
			world.draw()

			# Enquanto o jogador estiver no jogo
			if self.gameOver == 0:
				enemyGroup.update()
				# Atualização do placar, com checagem se a moeda foi coletada pelo jogador
				if pygame.sprite.spritecollide(player, coinGroup, True):
					self.totalScore += 1
					self.scoreInLevel += 1
					pygame.mixer.music.load('assets/sounds/coin.mp3')
					pygame.mixer.music.play(0)
				if pygame.sprite.spritecollide(player, keyGroup, True):
					self.keyCollected = 1
					pygame.mixer.music.load('assets/sounds/key.wav')
					pygame.mixer.music.play(0)
					exitGroup.update(self.keyCollected, self.daltonism)
				coinscoreText = text_format('X ' + str(self.totalScore), font, 30, white)
				keyscoreText = text_format('X ' + str(self.keyCollected), font, 30, white)
				coinscoreRect = coinscoreText.get_rect()
				screen.blit(coinscoreText, (60 - (coinscoreRect[2]/2), 5))
				keyscoreRect = keyscoreText.get_rect()
				screen.blit(keyscoreText, (160 - (keyscoreRect[2]/2), 5))
			if self.gameOver == 0:
				enemyGroup.update()

			enemyGroup.draw(screen)
			lavaGroup.draw(screen)
			coinGroup.draw(screen)
			exitGroup.draw(screen)
			keyGroup.draw(screen)
			vanityKey.draw(screen)
			vanityCoin.draw(screen)

			self.gameOver = player.update(self.gameOver, world, enemyGroup, lavaGroup, exitGroup, self.keyCollected, vanityCoin, vanityKey)

			# Caso o jogador morra
			if self.gameOver == -1:
				if restartButton.draw():
					world = World.reset_level(self.level, player, enemyGroup, lavaGroup, exitGroup, coinGroup, keyGroup, self.daltonism)
					self.gameOver = 0
					self.keyCollected = 0
					self.totalScore -= self.scoreInLevel
					self.scoreInLevel = 0
					scoreCoin = Coin(self.tile_size // 2 - 3, self.tile_size // 2 - 8, self.daltonism)
					scoreKey = Key(self.tile_size + 60, self.tile_size // 2 - 5, self.daltonism)
					vanityCoin.add(scoreCoin)
					vanityKey.add(scoreKey)

			# Caso o jogador ganhe
			if self.gameOver == 1:
				# Reset do jogo e ida ao proximo nivel
				self.level += 1
				self.scoreInLevel = 0
				coinGroup.remove(coinGroup)
				keyGroup.remove(keyGroup)
				# Caso ainda tenha mais níveis
				if self.level <= self.maxLevels:
					# Reset do nível
					world = World.reset_level(self.level, player, enemyGroup, lavaGroup, exitGroup, coinGroup, keyGroup, self.daltonism)
					self.gameOver = 0
					self.keyCollected = 0
					scoreCoin = Coin(self.tile_size // 2 - 3, self.tile_size // 2 - 8, self.daltonism)
					scoreKey = Key(self.tile_size + 60, self.tile_size // 2 - 5, self.daltonism)
					vanityCoin.add(scoreCoin)
					vanityKey.add(scoreKey)
				# Caso seja o último
				else:
					wonText = text_format('VOCE VENCEU!', font, 75, white)
					screen.blit(wonText, (600/2, -10))
					if restartButton.draw():
						# Reset do nível
						self.level = 1
						world = World.reset_level(self.level, player, enemyGroup, lavaGroup, exitGroup, coinGroup, keyGroup, self.daltonism)
						self.gameOver = 0
						self.keyCollected = 0
						self.totalScore = 0
						scoreCoin = Coin(self.tile_size // 2 - 3, self.tile_size // 2 - 8, self.daltonism)
						scoreKey = Key(self.tile_size + 60, self.tile_size // 2 - 5, self.daltonism)
						vanityCoin.add(scoreCoin)
						vanityKey.add(scoreKey)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			pygame.display.update()

		pygame.quit()
