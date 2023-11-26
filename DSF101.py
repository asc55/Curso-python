from datetime import date
def voto(ano):
    """
    Função que através do ano do nascimento vai dizer a situação eleitorial do usuario
    :param ano: Leitura do ano de nascimento de uma pessoa para calcular a sua idade
    :return: retorna a situação do voto eleitoral, de acordo com a idade calculada
    """
    idade = (date.today().year) - ano
    if idade < 16:
        s = 'VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        s = 'VOTO OPCIONAL'
    elif idade >= 18:
        s = 'VOTO OBRIGATÓRIO'
    print(f'Com {idade} anos: {s}')
    return s


"""nas = int(input('Ano de nascimento: '))
voto(nas)"""
help(voto)
"""help(voto)"""