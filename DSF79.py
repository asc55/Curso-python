listanum = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in listanum:
        listanum.append(valor)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valor duplicado, não vou adicionar...')
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N]').strip().upper()[0]
    if r == 'N':
        print(f'Você digitou os valores {sorted(listanum)}')
        break