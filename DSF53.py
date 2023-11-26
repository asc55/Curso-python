#Palíndromo
frase = input('Digite a frase a ser analisada: ').upper().replace(' ','')
inverso = ''
for letra in range(len(frase)-1, -1, -1):
    inverso += frase[letra]
print(frase,inverso)

""""invertida = frase [::-1]
#Não conseguir fazer com FOR
for i in frase:
    print(i,end='')
print('\n')
for i in invertida:
    print(i,end='')"""
if frase == inverso:
    print("É UM PALÍNDROMO")
else:
    print("NÃO É PALÍNDROMO")
