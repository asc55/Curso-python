nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print(nome.upper())
print(nome.lower())
print('Quantidade de caracteres sem os espaços: {}'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras...'.format(len(nome.split()[0])))
print('E esse primeiro nome é {}.'.format(nome.split()[0]))
#ou achar o primeiro espaço
print('O primeiro nome tem {} letras...'.format(nome.find(' ')))