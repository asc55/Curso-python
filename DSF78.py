valores = []
maior = nenor = 0
for cont in range (0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}:')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        elif valores[cont] < menor:
            menor = valores[cont]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posicoes: ',end='')
for pos, c in enumerate(valores):
    if c == maior:
        print(pos, end= '...')
print(f'\nO menor valor digitado foi {menor} nas posicoes: ',end='')
for pos, c in enumerate(valores):
    if c == menor:
        print(pos, end= '...')
#eu fiz uma lista pras posicoes tambem
"""posicoesma = []
posicoesme = []
for pos, c in enumerate(valores):
    if c == max(valores):
        posicoesma.append(pos)
    elif c == min(valores):
        posicoesme.append(pos)
print(f'O maior valor digitado foi {max(valores)} nas posições: ', end='')
for i in posicoesma:
    print(i, end='...')
print(f'\nO menor valor digitado foi {min(valores)} nas posições: ', end='')
for x in posicoesme:
    print(x, end='...')"""