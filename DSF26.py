frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase.. '.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.upper().find('A')+1))
print('A mesma letra aparece pela última vez na posição {}'.format(frase.upper().rfind('A')+1))