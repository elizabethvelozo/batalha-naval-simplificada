from random import randint
from interacao import *

ordem = 10

def gera_tabuleiro(qtde_navios):
    tabuleiro = [['□'] * ordem for i in range(ordem)]

    while qtde_navios > 0:
        # gera posição aleatória
        linha = randint(0, ordem - 1)
        coluna = randint(0, ordem - 1)

        # checa se a posição é válida
        ocorrencia = 0
        for i in range(linha - 1, linha + 2):
            if i < 0 or i > 9:
                continue
            for j in range(coluna - 1, coluna + 2):
                if j < 0 or j > 9:
                    continue
                if tabuleiro[i][j] == 'N':
                    ocorrencia += 1

        # aloca navio
        if ocorrencia == 0:
            tabuleiro[linha][coluna] = 'N'
            qtde_navios -= 1

    return tabuleiro

def verifica_coordenadas(coordenadas, tabuleiro_oponente):
    if tabuleiro_oponente[coordenadas[0]][coordenadas[1]] == 'N':
        resultado = 'FOGO'
        tabuleiro_oponente[coordenadas[0]][coordenadas[1]] = 'F'
    elif tabuleiro_oponente[coordenadas[0]][coordenadas[1]] == '□':
        resultado = 'ÁGUA'
        tabuleiro_oponente[coordenadas[0]][coordenadas[1]] = 'A'
    else:
        resultado = 'ERRO'

    return resultado

def jogada(nome_jogador, tabuleiro_oponente, navios_oponente):
    navios_afundados = 0
    while True:
        print(f'\n~~~~~~~~~~~~ Vez de {nome_jogador} ~~~~~~~~~~~~')
        exibe_tabuleiro(gera_espelho_tabuleiro(tabuleiro_oponente))
        coordenadas = pergunta_coordenadas()
        resultado = verifica_coordenadas(coordenadas, tabuleiro_oponente)

        print(f'{resultado}!')
        if resultado == 'FOGO':
            print('Você afundou um navio.')
            navios_afundados += 1
            if navios_afundados == navios_oponente:
                return navios_afundados
        elif resultado == 'ERRO':
            print('Essa coordenada já foi escolhida.')
            continue
        else:
            print('Você errou o tiro.')
            return navios_afundados