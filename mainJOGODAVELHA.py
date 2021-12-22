tabuleiro = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

usados = [0, 0, 0,
          0, 0, 0,
          0, 0, 0]

x = '\033[31mX\033[m'
o = '\033[36mO\033[m'

print(f'{"JOGO DA VELHA":-^42}')
print(f'{"Tabuleiro Inicial":^26}')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'{tabuleiro[i][j]:^5}', end='     ')
    print()
print()

while True:
    #   x jogando ************************************************************************************
    op = int(input(f'Onde deseja jogar? É a vez do {x}: '))
    print()

    while op < 1 or op > 9:
        op = int(input(f'Opção Inválida. '
                       f'Onde deseja jogar? '
                       f'É a vez do {x} '))
    while usados[op-1] == 'x' or usados[op-1] == 'o':
        op = int(input(f'Esta casa já foi escolhida.'
                       f'Onde deseja jogar? É a vez do {x} '))

    if op == 1:
        tabuleiro[0][0] = x
        usados[op-1] = 'x'
    elif op == 2:
        tabuleiro[0][1] = x
        usados[op-1] = 'x'
    elif op == 3:
        tabuleiro[0][2] = x
        usados[op-1] = 'x'
    elif op == 4:
        tabuleiro[1][0] = x
        usados[op-1] = 'x'
    elif op == 5:
        tabuleiro[1][1] = x
        usados[op-1] = 'x'
    elif op == 6:
        tabuleiro[1][2] = x
        usados[op-1] = 'x'
    elif op == 7:
        tabuleiro[2][0] = x
        usados[op-1] = 'x'
    elif op == 8:
        tabuleiro[2][1] = x
        usados[op-1] = 'x'
    elif op == 9:
        tabuleiro[2][2] = x
        usados[op-1] = 'x'

# CONDIÇÕES DE VITÓRIA PARA X SENDO VERIFICADAS APÓS CADA JOGADA

    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == x:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {x} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == x:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {x} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == x:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {x} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == x:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {x} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == x:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {x} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == x:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {x} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == x:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {x} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == x:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {x} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break



    for i in range(0, 3):
        for j in range(0, 3):
            print(f'{tabuleiro[i][j]:<}     ', end='')
        print()
    print()
#   O jogando ************************************************************************************

    op = int(input(f'Onde deseja jogar? É a vez do {o}: '))

    while op < 1 or op > 9:
        op = int(input(f'Opção inválida.'
                       f'Onde deseja jogar?'
                       f'É a vez do {o} '))
    while usados[op-1] == 'o' or usados[op-1] == 'x':
        op = int(input(f'Esta casa já foi escolhida.'
                       f'Onde deseja jogar?'
                       f'É a vez do {o} '))

    if op == 1:
        tabuleiro[0][0] = o
        usados[op-1] = 'o'
    elif op == 2:
        tabuleiro[0][1] = o
        usados[op-1] = 'o'
    elif op == 3:
        tabuleiro[0][2] = o
        usados[op-1] = 'o'
    elif op == 4:
        tabuleiro[1][0] = o
        usados[op-1] = 'o'
    elif op == 5:
        tabuleiro[1][1] = o
        usados[op-1] = 'o'
    elif op == 6:
        tabuleiro[1][2] = o
        usados[op-1] = 'o'
    elif op == 7:
        tabuleiro[2][0] = o
        usados[op-1] = 'o'
    elif op == 8:
        tabuleiro[2][1] = o
        usados[op-1] = 'o'
    elif op == 9:
        tabuleiro[2][2] = o
        usados[op-1] = 'o'
    print()

    # CONDIÇÕES DE VITÓRIA PARA O SENDO VERIFICADAS APÓS CADA JOGADA

    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == o:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {o} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == o:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {o} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == o:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {o} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == o:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {o} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == o:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {o} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == o:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {o} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == o:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {o} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == o:
        print(f'{"GAME OVER":^20}')
        print(f'{f"O {o} venceu: ":^26}')
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(f'{tabuleiro[i][j]:<}     ', end='')
            print()
        print()
        break

    for i in range(0, 3):
        for j in range(0, 3):
            print(f'{tabuleiro[i][j]:<}     ', end='')
        print()
    print()
