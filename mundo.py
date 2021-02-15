import pygame
from chave import Key
from lava import Lava
from saida import Exit
from moeda import Coin
from inimigo import Enemy

pygame.init()
screen = pygame.display.set_mode((900, 600))


# Classe do mundo
tile_size = 50


class World:
    def __init__(self, data, enemy_group, lava_group, coin_group, exit_group, key_group):
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

    @staticmethod
    def reset_level(level, player, enemy_group, lava_group, exit_group, coin_group, key_group):
        player.__init__(100, 600 - 130)
        enemy_group.empty()
        lava_group.empty()
        exit_group.empty()

        # load in level data and create world
        archive = open(f'levels/level{level}.txt', 'r')
        data = archive.read()
        archive.close()
        data = data.split('\n')
        world_data = []
        for num in range(0, 12):
            world_data.append(list(data[num]))

        world = World(world_data, enemy_group, lava_group, coin_group, exit_group, key_group)
        return world
