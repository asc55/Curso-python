n = input('Digite o que será dissecado: ')
print('Seu tipo primitivo é: ', type(n))
print('É numérico: ', n.isnumeric())
print('É alfabético:', n.isalpha())
print('É alfanumérico: ', n.isalnum())
print('É decimal: ', n.isdecimal())
print('É maiúsculo: ', n.isupper())
print('É minúsculo: ', n.islower())
print('É capitalizada: ', n.istitle())
print('É somente preenchida de espaços: ', n.isspace())