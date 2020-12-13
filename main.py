import pygame

pygame.init()
tela = pygame.display.set_mode((900, 600), 0)
pygame.display.set_caption("AVENTURA?")

direita = [pygame.image.load('imagens/R1.png'), pygame.image.load('imagens/R2.png'), pygame.image.load('imagens/R3.png'), pygame.image.load('imagens/R4.png'), pygame.image.load('imagens/R5.png'), pygame.image.load('imagens/R6.png'), pygame.image.load('imagens/R7.png'), pygame.image.load('imagens/R8.png'), pygame.image.load('imagens/R9.png')]
esquerda = [pygame.image.load('imagens/L1.png'), pygame.image.load('imagens/L2.png'), pygame.image.load('imagens/L3.png'), pygame.image.load('imagens/L4.png'), pygame.image.load('imagens/L5.png'), pygame.image.load('imagens/L6.png'), pygame.image.load('imagens/L7.png'), pygame.image.load('imagens/L8.png'), pygame.image.load('imagens/L9.png')]
fundo = pygame.image.load('imagens/bg1.jpg')
personagem = pygame.image.load('imagens/standing.png')

clock = pygame.time.Clock()

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()

        self.x = 600
        self.y = 530
        self.vel_x = 5
        self.vel_y = 5
        self.caminhada = 0
        self.pulo = 10
        self.verPulo = False
        self.verEsquerda = False
        self.verDireita = False

    def alterar_personagem(self, tela):
        if self.caminhada + 1 >= 27:
            self.caminhada = 0

        if self.verEsquerda:
            tela.blit(esquerda[self.caminhada // 3], (self.x, self.y))
            self.caminhada += 1
        elif  self.verDireita:
            tela.blit(direita[self.caminhada // 3], (self.x, self.y))
            self.caminhada += 1
        else:
            tela.blit(personagem, (self.x, self.y))

    def processar_teclas(self, teclas):
        if teclas[pygame.K_LEFT] and self.x > self.vel_x:
            self.x -= self.vel_x
            self.verEsquerda = True
            self.verDireita = False
        elif teclas[pygame.K_RIGHT] and self.x < 900 - self.vel_x - 32:
            self.x += self.vel_x
            self.verEsquerda = False
            self.verDireita = True
        else:
            self.verEsquerda = False
            self.verDireita = False
            self.caminhada = 0

        if not (self.verPulo):
            if teclas[pygame.K_SPACE]:
                self.verPulo = True
                self.verEsquerda = False
                self.verDireita = False
                self.caminhada = 0
        else:
            if self.pulo >= -10:
                negativo = 1
                if self.pulo < 0:
                    negativo = - 1
                self.y -= (self.pulo ** 2) * 0.5 * negativo
                self.pulo -= 1
            else:
                self.pulo = 10
                self.verPulo = False

def alterarPlanoFundo():
    tela.blit(fundo, (0, 0))
    jogador.alterar_personagem(tela)

    pygame.display.update()

if __name__ == "__main__":
    jogador = Character()

    rodando = True
    while rodando:
        clock.tick(27)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        posicaoJogador = (jogador.x, jogador.y)
        teclas = pygame.key.get_pressed()
        jogador.processar_teclas(teclas)
        alterarPlanoFundo()