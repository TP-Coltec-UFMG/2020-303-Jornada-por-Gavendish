import pygame

# Classe da moeda do jogo
tileSize = 50


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, daltonism):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(f'assets/img/{daltonism}/coin.png')
        self.image = pygame.transform.scale(img, (tileSize // 2, tileSize // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
