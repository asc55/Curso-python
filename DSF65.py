r = 's'
soma = maior = menor = c = 0
print('Digite n para parar!')
while r != 'n':
    n = int(input('Digite o número:'))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = input('Quer continuar? [ s / n }').lower()
print('A média de todos os {} valores digitados fica {:.2f}'.format(c,(soma/c)))
print('O maior valores digitado foi {}, o menor foi {}'.format(maior, menor))
