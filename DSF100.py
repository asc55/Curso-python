from random import randint
from time import sleep
def sorteio(s):
    print(f'Somando 5 valores da lista:', end=' ')
    for i in range(0,5):
        n = randint(1,100)
        s.append(n)
        print(f'{n} ',end='')
        sleep(0.1)
    print(' PRONTO!')


def somapares(sp):
    soma = 0
    for c in sp:
        if (c % 2) == 0:
            soma += c
    print(f'\nSomando os valores pares de {sp} temos ', end='')
    print(soma)
    print('\nFIM')


a = []
sorteio(a)
somapares(a)
