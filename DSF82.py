todos = []
pares = []
impares = []
#usando condicionais
"""while True:
    n = int(input('Digite um número: '))
    todos.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = ''
    r = input('Quer continuar? [S/N]:').strip().upper()[0]
    if r == 'N':
        print(f'A lista completa é {todos}')
        print(f'A lista de pares é {pares}')
        print(f'A lista de ímpares é {impares}')
        break"""
#usando for
while True:
    n = int(input('Digite um número: '))
    todos.append(n)
    r = ''
    r = input('Quer continuar? [S/N]:').strip().upper()[0]
    if r == 'N':
        break
for i in todos:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'A lista completa é {todos}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')