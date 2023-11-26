from random import randint
from time import sleep
print('JOGO DA MEGA SENA')
palpites = list()
dados = list()
n = int(input('Quantos jogos você quer que eu sorteie? '))
totol = 1
while totol <= n:
    cont = 0
    while True:
        palpite = randint(1,60)
        if palpite not in dados:
            dados.append(palpite)
            cont += 1
        if cont >= 6:
            break
    dados.sort()
    palpites.append(dados[:])
    dados.clear()
    totol += 1
"""print(f'Os números sorteados foram {palpites}')"""
for i, l in enumerate(palpites):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
"""for i in range(0,len(palpites)):
    print(f'Jogo {i+1}: {palpites[i]}')
    sleep(0.5)"""
#minha versão da questão
'''from random import randint
from time import sleep
print('JOGO DA MEGA SENA')
palpites = []
dados = []
n = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0,n):
    palpite = (randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60))
    dados.append(palpite)
    palpites.append(dados[:])
    dados.clear()
    print(f'Jogo {i+1}: ',end='')
    print(sorted(palpites[i]))
    sleep(0.5)
print('BOA SORTE')
'''