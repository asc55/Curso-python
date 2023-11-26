#boletim com listas compostas
listageral = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    listageral.append([nome,[n1,n2],media])
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [ S/N ]').strip().upper()[0]
    if r == 'N':
        print(listageral)
        break
print(f'{"N":<4}{"Nome do aluno":<10}{"Media":>8}')
for i, v in enumerate(listageral):
    print(f'{i+1:<4}{v[0]:<10}{v[2]:>8.1f}')
while True:
    op = int(input('Quer mostrar a nota de qual alunos? (999 interrompe)'))
    if op == 999:
        print('FINALIZANDO.... VOLTE SEMPRE')
        break
    elif op <= len(listageral):
        print(f'Notas do aluno {op} por nome {listageral[op-1][0]} são {listageral[op-1][1]}')