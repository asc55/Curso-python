#Brasileirão 2022
times = ('Palmeiras','Internacional','Fluminense','Corinthians',
         'Flamengo','Athletico-PR','Chapecoense','Fortaleza',
         'São Paulo','América-MG','Botafogo','Santos','Goiás',
         'Bragantino','Coritiba','Cuiabá','Ceará-SC','Atlético-GO','Avaí','Juventude')
"""print(f'Lista de times: {times}')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'\nOs últimos quatro colocados são: {times[-4:]}')"""
print('-=-'*25)
print('LISTA DE TIMES')
for t in times:
    print(t)
print('\nOs cinco primeiros colocados são:')
for c in range(0,5):
    print('\n',times[c], end='.')
print('\nOs quatro últimos colocados são:')
for i in range(-4,0):
    print('\n',times[i], end='.')
print(f'\nOs times em ordem alfabética fica {sorted(times)}')
posicao = times.index('Chapecoense')
print(f'O time chapecoense está na {posicao+1}a. posicao!')