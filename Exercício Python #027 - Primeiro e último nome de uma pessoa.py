n = str(input('Digite o seu nome:')).strip()
nome = n.split()
print('Muito prazer em te conhecer {}!'.format(nome[0]))
print('Seu primeiro nome é {}'.format(nome[0]))
if len (nome) > 1:
    print('Seu sobre nome é {}!'.format(nome[1]))
else:
    print('Você não escreveu seu sobre nome :(')
