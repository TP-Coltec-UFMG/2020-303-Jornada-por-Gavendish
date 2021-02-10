# Jornada por Gavendish
Jogo acessível feito com pygame. Grupo de Arthur Feu, Caio Augusto, Gustavo Paiva e João Lucas. A ideia do jogo é criar uma aventura em que o jogador busca um tesouro escondido em uma terra distante. Será um **platformer, com mecânica de combate simples e implementação de obstáculos** para dificultar a caminhada do personagem principal em busca de seu objetivo.

## Como executar?
Para executar o jogo, é recomendado que o usuário tenha a versão mais atualizada do Python3 e do GIT, para instalar o projeto. 
```
$ python3 --version
Python 3.8.6rc1

$ git --version
git version 2.24.0.windows.2
``` 
Além disso, recomenda-se também utilizar a IDE PyCharm para executar mais facilmente o código. Após criar um projeto novo (vazio) e baixar a pasta, ou cloná-la utilizando o seguinte comando
```
# Clonando o repositório principal do jogo
$ git clone https://github.com/TP-Coltec-UFMG/Jornada-por-Gavendish

# Instalando as dependências necessárias
$ pip3 install --requirement Jornada-por-Gavendish/requirements.txt
```
, o usuário deve fazer o seguinte:

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/img/comoexecutar.jpg">

> Para executar, basta que o usuário clique com o botão direito do mouse no arquivo *main.py* e clique em *Run 'main'*, na IDE PyCharm.
## Até o momento:
Até o momento, apenas duas funções foram implementadas: movimento do personagem principal e alteração do sprite, conforme o movimento, para dar animação. Além disso, uma fase básica foi criada, com plataformas para o usuário interagir. Sprites próprios foram criados, como o dos blocos, e sprites gratuito foram utilizados para construir o personagem e os inimigos.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/img/ateomomento1002.jpg">

> Imagem do dia 10/02 com o conteúdo atual do jogo, demonstrando o sprite do jogador, as plataformas já existentes, os inimigos, os obstáculos, as moedas e a porta de saída.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/img/ateomomento10022.jpg">

> Imagem do dia 10/02 mostrando quando o usuário morre, com o botão de reset aparecendo ao meio e a mensagem de GAME OVER acima.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/img/ateomomento10023.jpg">

> Imagem do dia 10/02 mostrando quando o usuário vence, com a mensagem de YOU WIN acima.

## Futuro:
Para o futuro próximo, fica planjeada a implementação da acessibilidade, com uma opção de descrição do cenário mais um modo alto contraste (ex.: cores esverdeadas explicitando a natureza em evidência ao longo do cenário). O alto contraste se daria pelo cenário e pelas plataformas em tons de cinza, com o nosso boneco azul e os inimigos vermelhos. Além disso, serão desenvolvidos também novos níveis.
