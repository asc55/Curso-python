from random import randint
from time import sleep
from operator import itemgetter
sorteios = {}
ranking = list()
sorteios['Jogador1'] = randint(1,6)
sorteios['Jogador2'] = randint(1,6)
sorteios['Jogador3'] = randint(1,6)
sorteios['Jogador4'] = randint(1,6)
for a, b in sorteios.items():
    print(f'O {a} tirou {b}')
    sleep(0.5)
print('Ranking dos jogadores: ')
ranking = sorted(sorteios.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}o. lugar: {v[0]} com {v[1]}.')
    sleep(1)