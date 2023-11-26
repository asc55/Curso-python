digitados = (int(input('Digite um número: ')), int(input('Digite um número: ')),
             int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'\nOs números digitados foram: ', end='')
for c in digitados:
    print(c, end=' ')
print(f'\nO valor 9 foi digitado {digitados.count(9)} vez(es)')
if 3 in digitados:
    posicao = digitados.index(3)
    print(f'O número 3 foi digitado na {posicao+1}a. posicao')
elif 3 not in digitados:
    print('O valor 3 não apareceu em nenhuma das posicoes..')
print('Os valores pares digitados foram: ', end='')
for par in digitados:
    if par % 2 == 0:
        print(par, end=' ')
