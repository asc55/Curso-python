#Formação de um triângulo
l1 = int(input("Digite o primeiro segmento do triângulo: "))
l2 = int(input('Digite o segundo segmento do triângulo: '))
l3 = int(input('Digite o terceiro segmento do triângulo:'))
if (l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2):
    print('Com as medidas {}, {} e {} podemos formar um triÂngulo'.format(l1,l2,l3))
else:
    print('Com as medidas {}, {} e {} não podemos formar um triÂngulo'.format(l1,l2,l3))