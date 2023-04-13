velha = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def menu():
    """
    Pergunta ao jogador se ele deseja jogar ou sair, sendo 0 a opção de saída
    e a opção 1 como iniciar jogo.
    :return: None
    """
    iniciar = 1
    while iniciar:
        iniciar = int(input("0. Sair \n"+"1. Jogar \n"))
        if iniciar:
            jogo()
        else:
            print("Saindo...")

def jogo():
    """
    Define as posições das jogadas (linhas e colunas) e identifica o ganhador.
    :return:None
    """
    jogada = 0 #Número de jogadas, +1 a cada rodada

    while ganhador() == 0:
        print("Jogador", jogada % 2 + 1) #Jogada % 2 = 0 e 1 alternando + 1 = 1 e 2 alternando = jogador 1 ou 2
        tabuleiro()
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        # Subtrai 1 para que o usuário possa usar as posições 1, 2 e 3
        if velha [linha-1][coluna-1] == 0:
            if(jogada % 2+1) == 1:
                velha[linha-1][coluna-1] = 1
            else:
                velha[linha-1][coluna-1] = -1
        else:
            print("Não está vazio")
            jogada -= 1

        if ganhador():
            print("Jogador", jogada % 2 + 1, "Ganhou após", jogada+1, "rodadas")
        jogada += 1

        if jogada > 8:
            print("Velha")
            break

def ganhador():
    """
    Checa se alguma linha, coluna ou diagonal está completa, se sim, apresenta o resultado, caso não,
    as rodadas continuam
    :return: Int
    """
    #Checar linhas
    for i in range(3):
        soma = velha[i][0]+velha[i][1]+velha[i][2]
        if soma == 3 or soma == -3:
            return 1

    #Checar colunas
    for i in range(3):
        soma = velha[0][i] + velha[1][i] + velha[2][i]
        if soma == 3 or soma == -3:
            return 1

    #Checar diagonais
    diagonal1 = velha[0][0]+velha[1][1]+velha[2][2]
    diagonal2 = velha[0][2]+velha[1][1]+velha[2][0]
    if diagonal1 == 3 or diagonal2 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1
    return 0

def tabuleiro():
    """
    Impressão do rabuleiro, o jogador 1 tem as jogadas representadas por números positivos = 1 =X
    o jogador 2 é representado por números negativos = -1 = O
    :return: None
    """
    for i in range(3):
        for j in range(3):
            if velha[i][j] == 0:
                print(" _ ", end=" ") #end não permite que pule de linha automaticamente
            elif velha[i][j] == 1:
                print(" X ", end=" ")
            elif velha[i][j] == -1:
                print(" O ", end=" ")
        print()

menu()
