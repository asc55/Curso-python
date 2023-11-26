#Progressão aritmética com WHILE
"""c = 9
a1 = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
print(a1, end='..')
while c > 0:
    proximo = (a1+razao)
    print(proximo, end='..')
    c -= 1
    a1 = proximo
print('  (esses são os 10 termos primeiros dessa P.A)')
n = int(input('Deseja mais quantos termos: \nobs: [ 0 ]para encerrar: '))+1
while n != 0:
    proximo = (a1+razao)
    print(proximo, end='..')
    a1 = proximo
    n -= 1
    if n == 1:
        n = int(input('\nmais quantos? \n[ 0 ] para encerrar: '))+1
        n = n
print('\nEncerrando...')"""
a1 = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
cont = 1
mais = 10
total = 0
termo = a1
while mais != 0:
    total += mais
    while cont <= total:
        print('{} '.format(termo),end='..')
        termo += razao
        cont += 1
    mais = int(input('\nMais quantos termos[0 para parar]: '))
print('Encerrando..')
print('Progressão finalizada com {} termos'.format(total))
