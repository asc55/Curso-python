matriz = [[0,0,0],[0,0,0],[0,0,0]]
somap = soma3c = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [ {l}, {c} ]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]} ]',end=' ')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
    print()
for l in range(0,3):
    soma3c += matriz[l][2]
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'A soma dos valores pares é {somap}')
print(f'A soma dos valores da terceira coluna é {soma3c}')
print(f'O maior valor da segunda linha é {maior}')