#maioridade
from datetime import date
maiores = 0
menores = 0
atual = date.today().year
for c in range(1,8):
    nasc = int(input('DIGITE O ANO DE NASCIMENTO da {} pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('Tenho {} pessoas maiores.'.format(maiores))
print('Tenho {} pessoas menores.'.format(menores))