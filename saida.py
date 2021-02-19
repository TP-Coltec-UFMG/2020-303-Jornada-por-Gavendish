import pygame


# Classe da porta de saida do nível
tileSize = 50


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y, daltonism):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(f'img/{daltonism}/exitlocked.png')
        self.image = pygame.transform.scale(img, (tileSize, int(tileSize * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.isLocked = True

    def update(self, keyCollected, daltonism):
        if keyCollected == 0:
            img = pygame.image.load(f'img/{daltonism}/exitlocked.png')
            self.image = pygame.transform.scale(img, (tileSize, int(tileSize * 1.5)))
        if keyCollected == 1:
            img = pygame.image.load(f'img/{daltonism}/exit.png')
            self.image = pygame.transform.scale(img, (tileSize, int(tileSize * 1.5)))

