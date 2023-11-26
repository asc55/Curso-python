valores = []
#usando for
for c in range(0,5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > valores[-1]:
        valores.insert(-1,v)
        print('Valor adicionado ao final da lista..')
    else:
        for i in range(0,len(valores)):
            if v <= valores[i]:
                valores.insert(i,v)
                print(f'Valor adicionado na posicao {i}')
#usando while
""" pos = 0
while pos < len(valores):
    if v <= valores[pos]:
        valores.insert(pos,v)
        print(f'Valor adicionado na posicao {pos} da lista...')
        break
    pos += 1"""
#usando somente if
"""if v < valores[0] or v == valores[0]:
    valores.insert(0,v)
    print('Valor adicionado na posicao 0 da lista...')
    valores[0] = v
elif v < valores[-1] and v > valores[0]:
    valores.insert(1,v)
    print(f'Valor adicionado na posicao 1..')
    valores[1] = v"""
print(f'Os valores adicionados em ordem foram {valores}')
