from random import randint
soma = qtd = 0
while True:
    pc = randint(1,10)
    vc = int(input('DIGA UM VALOR: '))
    soma = (pc+vc)
    opcao = ' '
    while opcao not in 'PI':
        opcao = input('PAR OU IMPAR: ').strip().upper()[0]
    if (soma % 2 == 0):
        if opcao == 'P':
            qtd += 1
            print(f'Sua jogada foi {vc} e a do computador {pc} (VOCê GANHOU! deu  PAR {soma})')
        elif opcao == 'I':
            print(f'Sua jogada foi {vc} e a do computador {pc} (VOCê PERDEU! deu  PAR {soma})')
            break
    else:
        if opcao == 'I':
            qtd += 1
            print(f'Sua jogada foi {vc} e a do computador {pc} (VOCê GANHOU! deu IMPAR {soma})')
        elif opcao == 'P':
            print(f'Sua jogada foi {vc} e a do computador {pc} (VOCê PERDEU! deu IMPAR {soma})')
            break
print(f'GAME OVER!!\nVocê venceu {qtd} vezes')