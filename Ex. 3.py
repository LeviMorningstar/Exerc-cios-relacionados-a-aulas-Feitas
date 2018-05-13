p1 = float(input('Qual o peso da primeira prova? '))
p2 = float(input('Qual o peso da Segunda prova? '))

n1 = float(input('Qual a nota da Primeira Prova? '))
n2 = float(input('Qual a nota da Segunda Prova? '))
print()
media_ponderada = ((n1 * p1) + (n2 * p2)) / (p1 + p2)
if media_ponderada >= 7:
    print ('A sua nota final é {:.2f}. Parabens você conseguiu colar o suficiente.'.format(media_ponderada))
else:
    print('A sua nota final é {:.2f}. Parabens você conseguiu rodar nessa porcaria de materia.'.format(media_ponderada))
print()
input('Aperte enter para sair')