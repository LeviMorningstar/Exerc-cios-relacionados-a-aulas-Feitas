print('Inicio do programa')

valid_nome = False
valid_notas = False
valid_faltas = False

pessoas = ['joao','maria','paulo','pedro']
print(pessoas)
while valid_nome == False:
    nome = input('Digite o nome completo do aluno: ').lower()
    if nome not in pessoas:
        print('Este aluno não costa no Banco de dados.')
    else:
        valid_nome = True

while valid_notas == False:
    nota1 = (input('Digite a Primeira nota do aluno: '))
    nota2 = (input('Digite a segunda nota do aluno: '))
    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
        if nota1 < 0 or nota1 >10:
            print('O valor da nota precisa ser entre 0,00 e 10,00')
        elif nota2 < 0 or nota2 >10:
            print('O valor da nota precisa ser entre 0,00 e 10,00')
        else:
            valid_notas = True
    except:
        print('Formado de texto inválido.')

while valid_faltas == False:
    faltas = (input('Digite o total de faltas do aluno: '))
    try:
        faltas = int(faltas)
        if faltas > 20 or faltas < 0:
            print('O numero de faltas excede o numero de aulas dadas.')
        else:
            valid_faltas = True
    except:
        print('Formato de Texto invalido.')

valid_faltas = False
valid_nome = False
valid_notas = False

media = (nota1 + nota2) / 2
assid = (20-faltas) /20
print('Nome:',nome)
print('Média:',media)
print('Assiduidade:',str(assid*100)+'%')
if faltas <= 6 or media >= 6.0:
    if faltas >= 6:
        print('Reprovado por faltas.')
    elif media < 6.0:
        print('Reprovado por Média.')
    else:
        print('Aprovado')
else:
    print ('Reprovado por faltas e por média.')


print()
input('Aperte enter para sair')