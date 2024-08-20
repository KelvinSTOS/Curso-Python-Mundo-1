import math
co = float(input('Tamanho do Cateto Oposto?'))
ca = float(input('Tamanho do Cateto Adjacente?'))
hi = math.hypot (co, ca)
print('A hipotebusa vai medir {:.2f}'.format(hi))
