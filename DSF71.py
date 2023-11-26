#Caixa eletronico
saque = int(input('Saque R$: '))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f' total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
"""qtd1 = qtd10 = qtd20 = qtd50 = 0
while True:
    saque = int(input('Qual o valor do saque desejado: '))
    qtd50 = (saque // 50)
    if qtd50 >= 1:
        print(f'Com esse valor de R${saque}, ficarei com {qtd50} notas de R$50,00')
    qtd20 = (saque % 50) // 20
    if qtd20 >= 1:
        print(f'{qtd20} notas de R$20,00')
    qtd10 = ((saque % 50) % 20) // 10
    if qtd10 >= 1:
        print(f'{qtd10} notas de R$10,00')
    qtd1 = (((saque % 50) % 20) % 10) // 1
    if qtd1 >= 1:
        print(f'{qtd1} notas de R$1,00')
    r = ' '
    while r not in 'NS':
        r = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if r == 'N':
        break
print('Fim do programa!!!')"""


