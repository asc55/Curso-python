situacoes = {}
situacoes['nome'] = str(input('Nome: '))
situacoes['media'] = float(input(f'Média de {situacoes["nome"]}: '))
if situacoes['media'] >= 7.0:
    situacoes['situacao'] = 'Aprovado'
elif 5.0 >= situacoes['media'] >= 6.9:
    situacoes['situacao'] = 'Recuperacao'
else:
    situacoes['situacao'] = 'Reprovado'
for a, b in situacoes.items():
    print(f'{a} é igual: {b}')