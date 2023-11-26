n1 = int(input('Digite o n1:'))
n2 = int(input('Digite o n2:'))
n3 = int(input('Digite o n3:'))
print('Os números digitados foram {}, {} e {}'.format(n1,n2,n3))
#Considerando um e testa dois
menor = maior = n1
if (n2 > n1 and n2 > n3):
    maior = n2
if (n3 > n1 and n3 > n2):
    maior = n3
if (n2 < n1 and n2 < n3):
    menor = n2
if (n3 < n1 and n3 < n2):
    menor = n3
print('O número menor é {}'.format(maior))
print('O número menor é {}'.format(menor))