todos = list()
soma = 0
mulheres = list()
while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [F/M]').upper().strip()[0]
        if pessoa ['sexo'] == 'F':
            mulheres.append(pessoa['nome'])
        if pessoa ['sexo'] in 'FM':
            break
        print('ERRO!!! Por favor, digite M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    todos.append(pessoa.copy())
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N]').strip().upper()[0]
    if r == 'N':
        print(todos)
        media = (soma/len(todos))
        print(f'O grupo tem {len(todos)} pessoas')
        print(f'A média de idade do grupo é {media:5.2f}')
        print(f'As mulheres cadastradas foram: ',end='')
        for i in mulheres:
            print(i, end=' ')
        print(f'\nLista de pessoas que estão acima da média: ')
        for i in todos:
           if i['idade'] > media:
               for a, b in i.items():
                print(f'{a} = {b} ',end='; ')
        break