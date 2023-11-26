from math import hypot
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
#h = (co ** 2) + (ca ** 2)
#hip = h ** (1/2)
hip = math.hypot(co,ca)
print('Para o cateto oposto de {} e o cateto adjacente de {},  a hipotenusa fica {:.2f}'.format(co,ca,hip))