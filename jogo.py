class jogo_velha:
    def __init__(self, mesa=[]): #Parametro opcional
        """
        Método construtor
        :param mesa: O parametro mesa é igual a matriz do tabuleiro do jogo da velha.
        """
        self.velha = mesa

    def iniciar(self):
        """
        Pergunta ao jogador se ele deseja jogar ou sair, sendo 0 a opção de saída
        e a opção 1 como iniciar jogo.
        :return: None
        """
        iniciar = 1
        while iniciar:
            iniciar = int(input("0. Sair \n"+"1. Jogar \n"))
            if iniciar:
                self.jogo()
            else:
                print("Saindo...")
    @property #Getter
    def mesa(self):
        """
        Puxa a variavel mesa.
        :return:Matriz
        """
        return self.mesa

    @mesa.setter #Setter
    def mesa(self, value):
        """
        Coloca a variavel.
        :param value:value
        :return:velha
        """
        self.velha = value

    def jogo(self):
        """
        Define as posições das jogadas (linhas e colunas) e identifica o jogador.
        :return:None
        """
        jogada = 0 #Número de jogadas, +1 a cada rodada
        velha_get = mesa

        while self.ganhador() == 0:
            print("Jogador", jogada % 2 + 1) #Jogada % 2 = 0 e 1 alternando + 1 = 1 e 2 alternando = jogador 1 ou 2
            self.__tabuleiro()
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            # Subtrai 1 para que o usuário possa usar as posições 1, 2 e 3
            if velha_get[linha-1][coluna-1] == 0:
                if(jogada % 2+1) == 1:
                    self.velha[linha-1][coluna-1] = 1
                else:
                    self.velha[linha-1][coluna-1] = -1
            else:
                print("Está posição ja está preenchida, escolha outra")
                jogada -= 1

            if self.ganhador():
                print("Jogador", jogada % 2 + 1, "Ganhou após", jogada+1, "rodadas")
            jogada += 1

            if jogada > 8:
                print("Velha")
                break


    def ganhador(self):
        """
        Checa se alguma linha, coluna ou diagonal está completa, se sim, apresenta o resultado, caso não,
        as rodadas continuam.
        :return: Int
        """
        #Checar linhas
        for i in range(3):
            soma = self.velha[i][0]+self.velha[i][1]+self.velha[i][2]
            if soma == 3 or soma == -3:
                return 1

        #Checar colunas
        for i in range(3):
            soma = self.velha[0][i] + self.velha[1][i] + self.velha[2][i]
            if soma == 3 or soma == -3:
                return 1

        #Checar diagonais
        __diagonal1 = self.velha[0][0]+self.velha[1][1]+self.velha[2][2] #Atributo privado
        __diagonal2 = self.velha[0][2]+self.velha[1][1]+self.velha[2][0]
        if __diagonal1 == 3 or __diagonal2 == -3 or __diagonal2 == 3 or __diagonal2 == -3:
            return 1
        return 0

    def __tabuleiro(self): #Metódo privado
        """
        Impressão do tabuleiro, o jogador 1 tem as jogadas representadas por números positivos = 1 =X
        o jogador 2 é representado por números negativos = -1 = O.
        :return: None
        """
        for i in range(3):
            for j in range(3):
                if self.velha[i][j] == 0:
                    print(" _ ", end=" ") #end não permite que pule de linha automaticamente
                elif self.velha[i][j] == 1:
                    print(" X ", end=" ")
                elif self.velha[i][j] == -1:
                    print(" O ", end=" ")
            print()


mesa = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

jogo_objeto = jogo_velha(mesa=mesa)
jogo_objeto.iniciar()
