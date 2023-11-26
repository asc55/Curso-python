#FATORIAL DE UM NÚMERO
#usando for
"""n = int(input('Fatorial de qual número: '))
acumulador = 1
for c in range(n,0,-1):
    acumulador *= c
    c -= 1
print('{}! é igual a: {}'.format(n, acumulador))"""
#usando while
n = int(input('Fatorial de qual número: '))
acumulador = 1
contador = n
while contador > 0:
    if contador > 1:
        print('{}'.format(contador), end='X')
    else:
        print('{}'.format(contador), end=' ')
    acumulador *= contador
    contador -= 1
print('\n{}! é igual a: {}'.format(n, acumulador))