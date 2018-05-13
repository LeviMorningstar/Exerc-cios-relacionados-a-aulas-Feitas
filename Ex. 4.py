print('Inicio do Programa')
print()
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maiol', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

data_nasc = input('Digite sua data de Nascimento no formato DD-MM-AAAA: ')

mes = int(data_nasc[3:5])
print()
print('Você nasceu no mês de {}'.format(meses[mes-1]))
print()
input('Aperte enter para sair')

