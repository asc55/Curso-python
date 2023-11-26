def fatorial(num=1, show=False):
    """
    :param num: número de input para calculo do fatorial
    :param show: quando True, mostra os cálculos
    :return: retorna o resultado do fatorial
    """
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(f'{i}',end='')
            if i > 1:
                print(f' X', end=' ')
            else:
                print(f' = ', end=' ')
        f *= i
    print(f)
    print(f'\nO fatorial de {n}! é = {f}')
    return f

n = int(input('Fatorial de: '))
fatorial(n,show=True)