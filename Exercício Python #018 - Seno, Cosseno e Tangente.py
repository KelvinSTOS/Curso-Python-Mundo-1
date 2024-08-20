import math
angulo = float(input('Digite o Ângulo '))
seno = math.sin(math.radians(angulo))
print('O Ângulo de {}, Mede {:.2f} SENO'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('O Angulo de {}, Mede {:.2f} Cosseno'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('O Angulo de {} Mede {:.2f} Tangente'.format(angulo, tan))
