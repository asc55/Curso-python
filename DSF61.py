#Progressão aritmética com WHILE
c = 9
a1 = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
print(a1, end='..')
while c > 0:
    proximo = (a1+razao)
    print(proximo, end='..')
    c -= 1
    a1 = proximo