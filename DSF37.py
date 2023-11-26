#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
#1 para binário, 2 para octal e 3 para hexadecimal
n = int(input('Digite um número inteiro: '))
print("""[ 1 ] converter para BINÁRIO 
[ 2 ] converter para OCTAL
[ 3 ] oonverter para HEXADECIMAL""")
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print("o numero {} em binário fica: {}".format(n, bin(n)[2:]))
elif opcao == 2:
    print("o numero {} em octal fica: {}".format(n, oct(n)[2:]))
elif opcao == 3:
    print("o numero {} em hexadecimal fica: {}".format(n,hex(n)))
else:
    print('Opcao inválida')