time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do jogador: "))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(1,tot+1):
        partidas.append(int(input(f'Quantos gols na partidas {c}? ')))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('Erro! Digite apenas S ou N...')
    if r == 'N':
        break
print('-=-' * 25)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k+1:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
print(time)
