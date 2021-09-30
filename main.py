from interacao import *
from logica import *

print('∗ ~~~ ∗ ~~~~~ ∗ ~~~~~~~ ∗ ~~~~~ ∗ ~~~ ∗')
print('             BATALHA NAVAL             ')
print('∗ ~~~ ∗ ~~~~~ ∗ ~~~~~~~ ∗ ~~~~~ ∗ ~~~ ∗')
print()

jogador_1 = pergunta_nome(1)
jogador_2 = pergunta_nome(2)

qtde_navios = pergunta_qtde_navios()

tabuleiro_jogador_1 = gera_tabuleiro(qtde_navios)
tabuleiro_jogador_2 = gera_tabuleiro(qtde_navios)

# Exibição dos tabuleiros originais para teste:
pergunta_exibe_teste(jogador_1, tabuleiro_jogador_1, \
    jogador_2, tabuleiro_jogador_2)

# PARTIDA
navios_jogador_1 = qtde_navios
navios_jogador_2 = qtde_navios

while True:
    # JOGADOR 1
    navios_afundados = jogada(jogador_1, tabuleiro_jogador_2, navios_jogador_2)
    navios_jogador_2 -= navios_afundados
    if navios_jogador_2 == 0:
        vencedor = jogador_1
        break

    # JOGADOR 2
    navios_afundados = jogada(jogador_2, tabuleiro_jogador_1, navios_jogador_1)
    navios_jogador_1 -= navios_afundados
    if navios_jogador_1 == 0:
        vencedor = jogador_2
        break

print(f'\nVencedor: {vencedor}')
print(f'\n~~~~~~~~~ Tabuleiro de {jogador_1} ~~~~~~~~~')
exibe_tabuleiro(tabuleiro_jogador_1)
print(f'\n~~~~~~~~~ Tabuleiro de {jogador_2} ~~~~~~~~~')
exibe_tabuleiro(tabuleiro_jogador_2)
print(f'\nFIM DE JOGO')
