qtdv = 0
valores = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    qtdv += 1
    r = ''
    r = input('Quer continuar: [S/N]').strip().upper()[0]
    if r == 'N':
        print(f'Você digitou {qtdv} elementos.')
        print(f'Os valores em ordem decrescente são {sorted(valores,reverse=True)}')
        if 5 in valores:
            print(f'O valor 5 foi encontrado na lista!')
        else:
            print(f'O valor 5 não foi encontrado na lista!')
        break