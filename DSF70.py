total = menor = cont = qtd = 0
nomebarato = ' '
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        qtd += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomebarato = nome
    r = ' '
    while r not in 'NS':
        r = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if r == 'N':
        break
print(f'O gasto total das compras é {total}')
print(f'A quantidade de produtos que custaram mais de mil reais é de {qtd} produtos')
print(f'O preco do produto mais barato é {menor} e o nome do produto é {nomebarato}')