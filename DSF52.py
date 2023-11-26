#primo
div = 0
n = int(input('Digite o número a ser analisado: '))
for c in range (1,n+1):
    if (n % c == 0):
        div += 1
        print('\033[33m', end='')
    else:
        print('\033[35m', end='')
    print('{}'.format(c),end=' ')
if div == 2:
    print('{} é PRIMO!'.format(n))
else:
    print('\n{} não é primo porque possui {} divisores'.format(n,div))