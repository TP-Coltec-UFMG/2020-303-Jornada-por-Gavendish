import pygame
pygame.init()

# Classe da lava, obstáculo do jogo
tileSize = 50


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y, daltonism):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(f'img/{daltonism}/lava.png')
        self.image = pygame.transform.scale(img, (tileSize, tileSize // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y