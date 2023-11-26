import random
n1 = input('nome do aluno 1: ')
n2 = input('nome do aluno 2: ')
n3 = input('nome do aluno 3: ')
n4 = input('nome do aluno 4:')
alunos = [n1, n2, n3, n4]
sorteado = random.choice(alunos)
print('O aluno sorteado dessa vez foi {}'.format(sorteado))
