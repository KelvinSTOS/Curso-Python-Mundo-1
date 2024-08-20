import random
al1 = str(input('Qual primeiro aluno?'))
al2 = str(input('Qual segundo aluno?'))
al3 = str(input('Qual terceiro aluno'))
sort = [al1, al2, al3]
escol = random.choice(sort)
print('O escolhido é {}'.format(escol))

