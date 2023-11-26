matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [ {l}, {c} ]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ]',end='')
    print(end='\n')
#usando while
"""cont = 0
while cont < 3:
    for m in matriz[cont]:
        print(f'[ {m} ]',end= '')
    print(end='\n')
    cont += 1"""
#usando for
"""for m in matriz[0]:
    print(f'[ {m} ]', end= '')
print('\n')
for m in matriz[1]:
    print(f'[ {m} ]', end= '')
print('\n')
for m in matriz[2]:
    print(f'[ {m} ]', end= '')"""
#OBS: dois for de alimentação e dois for de print!!!