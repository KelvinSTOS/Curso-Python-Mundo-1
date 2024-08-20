print('-=-' * 20)
r1 = float(input('Digite a 1º Linha : '))
r2 = float(input('Digite a 2º Linha : '))
r3 = float(input('Digite a 3º Linha : '))
print('=-=' * 20)
if  r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os Valores fornecidos PODEM formar um Tirângulo')
else:
    print('Os valores NÃO PODEM formar uma triângulo')
