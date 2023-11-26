#TriÂngulos
l1 = float(input('Digite a primeira reta do triângulo: '))
l2 = float(input('Digite a segunda reta do triângulo: '))
l3 = float(input('Digite a terceira reta do triângulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('O triângulo pode ser formado...')
    if l1 == l2 == l3:
        print('TRIÂNGULO EQUILÁTERO')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('TRIÂNGULO ISÓSCELES')
    else:
        print('TRIÂNGULO ESCALENO')
else:
    print('Não podemos formar um triângulo com esses segmentos...')