import pygame
# Classe do inimigo


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, daltonism):
        pygame.sprite.Sprite.__init__(self)
        self.imagesRight = []
        self.imagesLeft = []
        for num in range(1, 4):
            imgRight = pygame.image.load(f'assets/img/{daltonism}/enemy{num}.png')
            self.imagesRight.append(imgRight)
            imgLeft = pygame.transform.flip(imgRight, True, False)
            self.imagesLeft.append(imgLeft)
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

