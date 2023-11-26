def ficha(n, gols=0):
    if n == '':
        n ="<desconhecido>"
    if gols == '' or gols != str:
        gols = 0
    print(f'O jogador {n} fez {gols} gol(s) no campeonato.')
    return str(n), int(gols)


a = input('Nome do jogador: ')
b = input('Número de gols: ')
ficha(a,b)