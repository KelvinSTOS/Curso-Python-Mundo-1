def calcular_aumento(salario):
    if salario > 0:
        aumento = salario * 0.15
        novo_salario = salario + aumento
        return novo_salario
    else:
        return salario

s1 = float(input('Qual é o salário do funcionário? $'))
s2 = calcular_aumento(s1)
print('Um funcionário que ganhava {:.2f}$, com 15% de aumento, ganha {:.2f}$'.format(s1, s2))
