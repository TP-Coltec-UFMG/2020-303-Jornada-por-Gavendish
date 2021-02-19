import pygame
from chave import Key
from lava import Lava
from saida import Exit
from moeda import Coin
from inimigo import Enemy

pygame.init()
screen = pygame.display.set_mode((900, 600))


# Classe do mundo
tileSize = 50


class World:
    def __init__(self, data, enemy_group, lava_group, coin_group, exit_group, key_group, daltonism):
        self.tile_list = []
        # Carregando as imagens de blocos
        dirtImg = pygame.image.load(f'img/{daltonism}/dirt.jpg')
        grassImg = pygame.image.load(f'img/{daltonism}/grass.jpg')
        platformImg = pygame.image.load(f'img/{daltonism}/platform.jpg')
        platformwograssImg = pygame.image.load(f'img/{daltonism}/platform2.jpg')
        rowCount = 0
        for row in data:
            colCount = 0
            for tile in row:
                if tile == '1':
                    img = pygame.transform.scale(dirtImg, (tileSize, tileSize))
                    imgRect = img.get_rect()
                    imgRect.x = colCount * tileSize
                    imgRect.y = rowCount * tileSize
                    tile = (img, imgRect)
                    self.tile_list.append(tile)
                if tile == '2':
                    img = pygame.transform.scale(grassImg, (tileSize, tileSize))
                    imgRect = img.get_rect()
                    imgRect.x = colCount * tileSize
                    imgRect.y = rowCount * tileSize
                    tile = (img, imgRect)
                    self.tile_list.append(tile)
                if tile == '3':
                    img = pygame.transform.scale(platformImg, (tileSize, tileSize))
                    imgRect = img.get_rect()
                    imgRect.x = colCount * tileSize
                    imgRect.y = rowCount * tileSize
                    tile = (img, imgRect)
                    self.tile_list.append(tile)
                if tile == '4':
                    img = pygame.transform.scale(platformwograssImg, (tileSize, tileSize))
                    imgRect = img.get_rect()
                    imgRect.x = colCount * tileSize
                    imgRect.y = rowCount * tileSize
                    tile = (img, imgRect)
                    self.tile_list.append(tile)
                if tile == '5':
                    enemy = Enemy(colCount * tileSize, rowCount * tileSize + 12, daltonism)
                    enemy_group.add(enemy)
                if tile == '6':
                    lava = Lava(colCount * tileSize, rowCount * tileSize + (tileSize // 2), daltonism)
                    lava_group.add(lava)
                if tile == '7':
                    coin = Coin(colCount * tileSize + (tileSize // 2), rowCount * tileSize + (tileSize // 2), daltonism)
                    coin_group.add(coin)
                if tile == '8':
                    exitdoor = Exit(colCount * tileSize, rowCount * tileSize - (tileSize // 2), daltonism)
                    exit_group.add(exitdoor)
                if tile == '9':
                    key = Key(colCount * tileSize, rowCount * tileSize - (tileSize // 2), daltonism)
                    key_group.add(key)
                colCount += 1
            rowCount += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

    @staticmethod
    def reset_level(level, player, enemyGroup, lavaGroup, exitGroup, coinGroup, keyGroup, daltonism):
        player.__init__(100, 600 - 130, daltonism)
        enemyGroup.empty()
        lavaGroup.empty()
        exitGroup.empty()

        # load in level data and create world
        archive = open(f'levels/level{level}.txt', 'r')
        data = archive.read()
        archive.close()
        data = data.split('\n')
        world_data = []
        for num in range(0, 12):
            world_data.append(list(data[num]))

        world = World(world_data, enemyGroup, lavaGroup, coinGroup, exitGroup, keyGroup, daltonism)
        return world
