from random import randrange

def display_board(board):
 # A função aceita um parâmetro contendo o status atual do tabuleiro
 # e o imprime no console.

 strb = "+----------+----------+----------+"
 strp = "|          |          |          |"

 i = 1
 
 print(f"{strb}\n", end="")
 for linha in board:
    print(f"{strp}\n|", end="")
    for elem in linha:
        if elem == "":
            print(f"    {i}     |", end="")
        else:
            print(f"    {elem}     |", end="")
        i+=1

    print(f"\n{strp}\n", end="")
    print(f"{strb}")

def enter_move(board):
 # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
 # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.

    linhas = len(board[0])
    colunas = len(board)

    jogada = int(input("Digite sua jogada(1 - 9): "))

    if  jogada < 0 or jogada > 10:
        print("Posição inválida")
        return

    jogada-=1

    linha_jogada = jogada // linhas
    coluna_jogada = jogada % colunas

    livres = make_list_of_free_fields(board=board)
    if (linha_jogada, coluna_jogada) not in livres:
        print("Essa posição já foi marcada")
        return 

    board[linha_jogada][coluna_jogada] = "O"

    display_board(board=board)
    

def make_list_of_free_fields(board):
 # A função navega pelo tabuleiro e constrói uma lista de todas as casas livres; 
 # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.

    livres = []
    i = 0
    for linha in board:
        j = 0
        for elem in linha:
            if elem == "":
                livres.append((i, j))
            j+=1
        i+=1

            
    return livres

def victory_for(board, sign):
    # A função analisa o estado do tabuleiro a fim de verificar se 
    # o jogador usando 'O's ou 'X's ganhou o jogo
    colunas = len(board)
    linhas = colunas

    for rc in range(linhas):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:	# verifica a linha rc
            return True
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign: # verifica a coluna rc
            return True

    diagonal_1, diagonal_2 = True, True
    for rc in range(linhas):
        if board[rc][rc] != sign: # verifica a primeira diagonal
            diagonal_1 = False
        if board[rc][2 - rc] != sign: # verifica a segunda diagonal
            diagonal_2 = False
    
    return diagonal_1 or diagonal_2

def draw_move(board):
    # A função desenha o movimento do computador e atualiza o tabuleiro.
    escolha_sucedida = False
    linhas = len(board[0])
    colunas = len(board)

    livres = make_list_of_free_fields(board=board)

    linhas_meio, coluna_meio = 1, 1
    # se meio está livre
    if (linhas_meio, coluna_meio) in livres:
        board[linhas_meio][coluna_meio] = "X"
        display_board(board=board)
        return

    while escolha_sucedida is not True:
        num = randrange(0, 8)   
        linha_computador = num // linhas
        coluna_computador = num % colunas
        if (linha_computador, coluna_computador) in livres:
            escolha_sucedida = True

    board[linha_computador][coluna_computador] = "X"

    display_board(board=board)

def init_board():
    # cria tabuleiro
    linhas, colunas = 3, 3
    board = []
    EMPTY = ""
    for i in range(linhas):
        linha = [EMPTY for i in range(colunas)]
        board.append(linha)

    return board

def main():
    vez_jogador = False
    rodando = True
    idx = 0
    simbolos = ["X", "O"]

    board = init_board()

    while rodando:
        if vez_jogador:
            move_jogador = enter_move(board=board)
            if move_jogador is False:
                continue
        else:
            draw_move(board=board)

        resultado = victory_for(board=board, sign=simbolos[idx])
        livres = make_list_of_free_fields(board=board)

        if resultado: 
            print(f"{simbolos[idx]} ganhou!")
            rodando = False
        elif len(livres) == 0:
            print("Velha")
            rodando = False

        idx = (idx + 1) % 2
        vez_jogador = not vez_jogador

if __name__ == "__main__":
    main()