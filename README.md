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

Caso seja necessário, selecione o interpretador correto:

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/img/comoexecutar2.jpg">

## Até o momento:
Até o momento, apenas duas funções foram implementadas: movimento do personagem principal e alteração do sprite, conforme o movimento, para dar animação. Além disso, uma fase básica foi criada, com plataformas para o usuário interagir. Sprites próprios foram criados, como o dos blocos, e sprites gratuito foram utilizados para construir o personagem e os inimigos.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/img/ateomomento11021.jpg">

> Imagem do dia 11/02 com o nível 1 do jogo, mostrando o sprite do jogador, as plataformas já existentes, os inimigos, os obstáculos, as moedas, a chave e a porta de saída (trancada).

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/img/ateomomento11022.jpg">

> Imagem do dia 10/02 mostrando a porta aberta, quando o usuário pega a chave.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/img/ateomomento11023.jpg">

> Imagem do dia 11/02 mostrando o nível 2 do jogo.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/img/ateomomento11024.jpg">

> Imagem do dia 11/02 mostrando a morte do jogador.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/img/ateomomento11025.jpg">

> Imagem do dia 11/02 mostrando a vitória do jogador.

## Futuro:
Para o futuro próximo, fica planjeada a implementação da acessibilidade, com uma opção de descrição do cenário mais um modo alto contraste (ex.: cores esverdeadas explicitando a natureza em evidência ao longo do cenário). O alto contraste se daria pelo cenário e pelas plataformas em tons de cinza, com o nosso boneco azul e os inimigos vermelhos. Além disso, serão desenvolvidos também novos níveis.
