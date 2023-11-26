import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Com base no ângulo {}, o seno fica {:.2f}, o cosseno fica {:.2f} e a tangente fica {:.2f}'.format(angulo,seno,cosseno,tangente))