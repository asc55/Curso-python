def area(b, c):
    a = (b * c)
    print(f'{a}',end='')


b = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))
print(f'A área do terreno de {b} x {c} é de ',end='')
area(b,c)
print(' metros quadrados')