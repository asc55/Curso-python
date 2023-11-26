from datetime import date
dados = {'nome': input('Nome: ')}
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = (atual-nasc)
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratacao'] + 35) - nasc
    print(dados)
    for a,b in dados.items():
        print(f'{a} = {b}')
else:
    print(dados)
    for a, b in dados.items():
        print(f'{a} = {b}')