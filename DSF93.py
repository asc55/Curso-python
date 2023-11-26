dados = {'nome': input('Nome do Jogador:')}
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?'))
gol = list()
tot = 0
for c in range(1, partidas+1):
    p = int(input(f'Quantos gols na partida {c}?'))
    gol.append(p)
    tot += p
dados['gols'] = gol.copy()
dados['total'] = tot
print(dados)
for a, b in dados.items():
    print(f' {a} = {b}')
print(f'O Jogador {dados["nome"]} jogou {partidas} partidas')
for v in range(1,partidas+1):
    print(f'Na partida {v}, fez {dados["gols"][v-1]} gols')