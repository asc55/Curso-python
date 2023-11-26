#Validando expressões matemáticas
lista = []
expressao = input('Digite a frase a ser analisada: ')
for letra in expressao:
    if letra == '(':
        lista.append('(')
    elif letra == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Expressão matemática válida!')
else:
    print('Expressão matemática inválida...')

"""#usando o count
for i in expressao:
    lista.append(i)
if lista.count('(') == lista.count(')'):
    print('A expressão é válida, com a mesma quantidade de parênteses abertos e fechados')
else:
    print('Há um desequilíbrio na quantidade de parênteses...')"""

"""#usando condicionais
if lista[-1] == ')' and lista[0] == '(' and lista[-2] != ')' and lista[1] != '(':
    print('A frase está válida!!')
else:
    print('A frase está inválida...')
"""