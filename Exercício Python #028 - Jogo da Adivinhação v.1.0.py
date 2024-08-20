from random import randint
computador = randint (0, 10)
from time import sleep
print('=-=' * 20)
print('Vou pensa em um número de 0 a 10 e você tenta advinhar!')
print('=-=' * 20)
jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(24)
if jogador == computador:
    print('Parabéns! Acertou mizeravi.')
else:
    print('Errou! Pensei no número {}, e não no {} kkkk :)'.format(computador, jogador))
