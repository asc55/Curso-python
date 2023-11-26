#contando vogais em uma tupla
palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos: ', end='')
    for c in i:
        if c in 'aeiou':
            print(f'{c} ', end='')