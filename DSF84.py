pessoas = list()
dados = list()
maior = menor = 0
maiorpeso = []
menorpeso = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    if len(pessoas) == 1:
        maior = menor = pessoas[0][1]
    r = ' '
    while r not in 'NS':
        r = input('Quer continuar? [S/N]').strip().upper()[0]
    if r == 'N':
        for p in pessoas:
            if p[1] > maior:
                maior = p[1]
            elif p[1] < menor:
                menor = p[1]
        for p in pessoas:
            if p[1] == maior:
                maiorpeso.append(p[0])
            elif p[1] == menor:
                menorpeso.append(p[0])
        break
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso digitado foi {maior}KG de {maiorpeso}')
print(f'O menor peso digitado foi {menor}KG de {menorpeso}')