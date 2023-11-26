lista = [[],[]]
for c in range(1,8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if (valor % 2 == 0):
        lista[0].append(valor)
    elif (valor % 2 == 1):
        lista[1].append((valor))
print(f'Os valores digitados foram {(lista)}')
print(f'Os valores pares digitados foram {sorted(lista[0])}')
print(f'Os valores impares digitados foram {sorted(lista[1])}')
