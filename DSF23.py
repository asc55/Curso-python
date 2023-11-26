# Como String
"""numero = input('Digite o número: ')
print('Unidade: ', numero[-1])
print('Dezena: ', numero[-2])
print('Centena: ', numero[-3])
print('Milhar: ', numero[-4])"""

# Com matemática
numero = int(input('Digite o número: '))
M = (numero//1000)
C = (numero%1000)//100
D = (numero%100)//10
U = (numero%10)//1
print('Milhar: ', M)
print('Centena: ', C)
print('Dezena: ', D)
print('Unidade: ', U)
