#Confederação Nacional de Natação
from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = (ano - nasc)
print('{} anos de idade'.format(idade))
if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade <= 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')