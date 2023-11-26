from datetime import date
# cálculo do ano bissexto
"""from calendar import isleap

ano = int(input('Digite o ano a ser consultado: '))
if isleap(ano) == True:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))"""

ano = int(input('Digite o ano a ser consultado ou 0 para ano atual:'))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é Bissexto!!'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))
