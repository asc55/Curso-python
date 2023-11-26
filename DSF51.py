"""a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da PA: '))
print(a1,end='..')
for c in range(0,9):
    proximo = (a1 + r)
    print(proximo, end= '..')
    a1 = proximo"""
#fiz aqui com for e vou fazer com auxílio da matemática
primeiro = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c),end='..')