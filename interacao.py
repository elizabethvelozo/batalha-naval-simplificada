ordem = 10

def pergunta_nome(jogador):
    nome_jogador = input(f'Jogador {jogador}: ')
    nome_jogador = nome_jogador.capitalize()

    return nome_jogador

def pergunta_qtde_navios():
    while True:
        qtde_navios = input('Qtde. de navios[máx. 10]: ')
        if not qtde_navios.isnumeric():
            print('Insira um valor numérico.')
            continue

        qtde_navios = int(qtde_navios)
        if qtde_navios < 1 or qtde_navios > 10:
            print('Insira pelo menos 1 navio e no máximo \n10.')
            continue
        else:
            return qtde_navios

def exibe_tabuleiro(tabuleiro):
    print(f'\n      0  1  2  3  4  5  6  7  8  9')
    for linha in range(ordem):
        print(f'   {chr(linha + 65):3}', end='')
        for coluna in range(ordem):
            print(f'{tabuleiro[linha][coluna]:3}', end='')
        print()

def pergunta_exibe_teste(nome_jogador_1, tabuleiro_1, nome_jogador_2, tabuleiro_2):
    resposta = input('\nDeseja exibir tabuleiros para teste \n[S/N]? ')
    resposta = resposta.upper()

    if resposta == 'S':
        print(f'\n~~~~~~~~~ Tabuleiro de {nome_jogador_1} ~~~~~~~~~')
        exibe_tabuleiro(tabuleiro_1)
        print(f'\n~~~~~~~~~ Tabuleiro de {nome_jogador_2} ~~~~~~~~~')
        exibe_tabuleiro(tabuleiro_2)

def gera_espelho_tabuleiro(tabuleiro):
    espelho_tabuleiro = [[None] * ordem for i in range(ordem)]

    for linha in range(ordem):
        for coluna in range(ordem):
            if tabuleiro[linha][coluna] != 'A' and tabuleiro[linha][coluna] != 'F':
                espelho_tabuleiro[linha][coluna] = '□'
            else:
                espelho_tabuleiro[linha][coluna] = tabuleiro[linha][coluna]

    return espelho_tabuleiro

def pergunta_coordenadas():
    while True:
        coordenadas = input('\nEscolha as coordenadas [A-J][0-9]: ')
        if len(coordenadas) != 2:
            print('São necessárias duas coordenadas.')
            continue

        coordenada_1 = coordenadas[0]
        coordenada_2 = coordenadas[1]
        if not coordenada_1.isalpha() or not coordenada_2.isnumeric():
            print('Insira uma coordenada no formato \n[letra][número].')
            print('Exemplo: A0')
            continue

        coordenada_1 = ord(coordenada_1.upper()) - 65
        coordenada_2 = int(coordenada_2)
        if coordenada_1 > 9:
            print('Insira uma coordenada de A a J \ne outra de 0 a 9.')
            continue

        coordenadas = [None] * 2
        for i in range(2):
            coordenadas[0] = coordenada_1
            coordenadas[1] = coordenada_2

        return coordenadas