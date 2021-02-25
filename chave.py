import pygame
pygame.init()

# Classe da chave do jogo
tileSize = 50


class Key(pygame.sprite.Sprite):
    def __init__(self, x, y, daltonism):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(f'assets/img/{daltonism}/key.png')
        self.image = pygame.transform.scale(img, (tileSize, tileSize // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
