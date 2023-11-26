from random import randint
sorteio = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os números sorteados foram: ',end='')
for s in sorteio:
    print(s,end=' ')
print(f'\nO maior número sorteado foi {max(sorteio)}')
print(f'O menor número sorteado foi {min(sorteio)}')
