def leiaint(n):
    while True:
        if n.isnumeric():
            resp = print(f'O número digitado {n} SERÁ lido como inteiro')
            return resp
        print(f'O que foi digitado {n} NÃO PODE ser lido como inteiro.')
        n = input('Digite um número válido:')


num = leiaint(input('Digite o que será consultado: '))




