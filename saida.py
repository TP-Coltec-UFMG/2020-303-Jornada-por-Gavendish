import pygame


# Classe da porta de saida do nível
tile_size = 50


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/exitlocked.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.isLocked = True

    def update(self, keyCollected):
        if keyCollected == 0:
            img = pygame.image.load('img/exitlocked.png')
            self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        if keyCollected == 1:
            img = pygame.image.load('img/exit.png')
            self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))

