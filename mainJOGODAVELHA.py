def f_op(jogador):  # jogador escolhe posição de jogada e ela é validada entre as jogadas disponíveis

    op = int(input(f'Onde deseja jogar? É a vez do {jogador}: '))
    while op < 1 or op > 9:
        op = int(input(f'Opção inválida.'
                       f'Onde deseja jogar?'
                       f'É a vez do {jogador} '))

    while usados[op-1] == 'x' or usados[op-1] == 'o':
        op = int(input(f'Esta casa já foi escolhida.'
                       f'Onde deseja jogar? É a vez do {jogador} '))
    return op


def tabuleiro_recebendo_jogada(escolha_do_jogador, x_ou_o):  # escolha do jogar é validada e atribuída ao tabuleiro
    for i in range(0, 3):
        for j in range(0, 3):
            if tabuleiro[i][j] == escolha_do_jogador:
                tabuleiro[i][j] = x_ou_o
                if x_ou_o == '\033[31mX\033[m':
                    usados[escolha_do_jogador - 1] = 'x'
                else:
                    usados[escolha_do_jogador - 1] = 'o'


def imprimi_tab():  # imprime o tabuleiro
    for ii in range(0, 3):
        for jj in range(0, 3):
            print(f'{tabuleiro[ii][jj]} ', end='     ')
        print()
    print()


global tabuleiro, usados, x, o

tabuleiro = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
usados = [0, 0, 0,
          0, 0, 0,
          0, 0, 0]

x = '\033[31mX\033[m'
o = '\033[36mO\033[m'
print('='*44)
print(f'{"JOGO DA VELHA":-^44}')
print(f'{"TIC TAC TOE":-^44}')
print('='*44)
print()
print(f'{"Tabuleiro Inicial:"}')

imprimi_tab()
print()

while True:
    # x jogando ************************************************************************************

    tabuleiro_recebendo_jogada(f_op(x), x)
    print()
    imprimi_tab()

# CONDIÇÕES DE VITÓRIA PARA 'X' SENDO VERIFICADAS APÓS CADA JOGADA

    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == x or \
            tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == x or \
            tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == x or \
            tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == x or \
            tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == x or \
            tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == x or \
            tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == x or \
            tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == x:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {x} venceu: ":^26}')
        break
# O jogando ************************************************************************************

    tabuleiro_recebendo_jogada(f_op(o), o)
    print()
    imprimi_tab()

    # CONDIÇÕES DE VITÓRIA PARA 'O' SENDO VERIFICADAS APÓS CADA JOGADA

    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == o or \
            tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == o or \
            tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == o or \
            tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == o or \
            tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == o or \
            tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == o or \
            tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == o or \
            tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == o:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {o} venceu: ":^26}')
        print()
        break
