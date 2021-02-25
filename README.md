# Jornada por Gavendish
Jogo acessível feito com pygame. Grupo de Arthur Feu, Caio Augusto, Gustavo Paiva e João Lucas. A ideia do jogo é criar uma aventura em que o jogador busca um tesouro escondido em uma terra distante. Será um **platformer com obstáculos** para dificultar a caminhada do personagem principal em busca de seu objetivo.

## Como executar?
Para executar o jogo, é recomendado que o usuário tenha a versão mais atualizada do Python3 e do GIT, para instalar o projeto. 
```
$ python3 --version
Python 3.8.6rc1

$ git --version
git version 2.24.0.windows.2
``` 
Além disso, é necessário utilizar a IDE PyCharm para executar o código, já que ocorre um erro ao tentar executar o programa pelo terminal. Após criar um projeto novo (vazio) e baixar a pasta, ou cloná-la utilizando o seguinte comando
```
# Clonando o repositório principal do jogo
$ git clone https://github.com/TP-Coltec-UFMG/Jornada-por-Gavendish

# Instalando as dependências necessárias
$ pip3 install --requirement Jornada-por-Gavendish/requirements.txt
```
, o usuário deve fazer o seguinte:

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/comoexecutar.jpg">

> Para executar, basta que o usuário clique com o botão direito do mouse no arquivo *menu.py* e clique em *Run 'menu'*, na IDE PyCharm. 

Caso seja necessário, selecione o interpretador correto:

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/comoexecutar2.jpg">

## Até o momento:
Até o momento, os seguintes elementos foram implementados: movimento do personagem principal e alteração do sprite, conforme o movimento, para dar animação. Além disso, uma fase básica foi criada, com plataformas para o usuário interagir. Sprites próprios foram criados, como o dos blocos, e sprites gratuito foram utilizados para construir o personagem e os inimigos. Sons disponibilizados gratuitamente na internet foram utilizados para compor os efeitos especiais do jogo. Além disso, os sprites também foram adaptados para os daltonismos existentes, que são os seguintes:

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/daltonismotipos.png">

> Imagem mostrando os tipos de daltonismos e qual cor eles impactam.

Agora imagens do jogo em si:

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/menu1.jpg">

> Imagem mostrando o menu do jogo.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/menu2.jpg">

> Imagem mostrando o submenu de seleção do modo de jogo, de acordo com a necessidade do usuário.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/telanormal.jpg">

> Imagem mostrando a tela sem filtros de daltonismo.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/telaprotanopia.jpg">

> Imagem mostrando a tela com o filtro de protanopia.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/teladeuteranopia.jpg">

> Imagem mostrando a tela com o filtro de deuteranopia.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/telatritanopia.jpg">

> Imagem mostrando a tela com o filtro de tritanopia.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/morte.jpg">

> Imagem mostrando a tela após a morte do jogador.
> 
<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/nivel1.jpg">

> Imagem mostrando o nível 1 do jogo.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/nivel2.jpg">

> Imagem mostrando o nível 2 do jogo.

<img src = "https://github.com/TP-Coltec-UFMG/JACP/blob/main/assets/img/vitoria.jpg">

> Imagem mostrando a vitória do jogador.

## Futuro:
Para o futuro próximo, fica planjeada a implementação da acessibilidade, com uma opção de descrição do cenário mais um modo alto contraste (ex.: cores esverdeadas explicitando a natureza em evidência ao longo do cenário). O alto contraste se daria pelo cenário e pelas plataformas em tons de cinza, com o nosso boneco azul e os inimigos vermelhos. Além disso, serão desenvolvidos também novos níveis. Pode-se perceber também que os sprites, ao serem adaptados para os filtros de daltonismo, perdem um pouco da qualidade, logo sendo necessário um melhor polimento.
