
def IMC(peso,altura):
    IMC = peso / (altura*altura)
    return IMC

def class_imc(sexo,peso,altura):
    valor_imc = IMC(peso,altura)
    if sexo == 'm':
        if valor_imc < 20.7:
            return 'Abaixo do peso.'
        elif valor_imc >= 20.7 and valor_imc <= 26.4:
            return 'No peso Normal.'
        elif valor_imc > 26.4 and valor_imc <= 27.8:
            return 'Marginalmente aceima do Peso.'
        elif valor_imc > 27.8 and valor_imc <= 31.1:
            return 'Acima do peso Ideal.'
        else:
            return 'Obeso.'
    elif sexo == 'f':
        if valor_imc < 19.1:
            return 'Abaixo do peso.'
        elif valor_imc >= 19.1 and valor_imc <= 25.8:
            return 'No peso Normal.'
        elif valor_imc > 25.8 and valor_imc <= 27.3:
            return 'Marginalmente aceima do Peso.'
        elif valor_imc > 27.3 and valor_imc <= 32.3:
            return 'Acima do peso Ideal.'
        else:
            return 'Obeso.'

print('Vamos Calcular o IMC?')

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite o Seu sexo, M para masculino ou F para feminino: ').lower()
    if sexo != 'm' and sexo !='f':
        print('Erro na entrada de dados, por favor Ultilize um formato valido.')
    else:
        valid_sexo = True
        print('\n')

valid_altura = False
while valid_altura == False:
    altura = input('Digite sua Altura: ')
    try:
        altura = float(altura)
        valid_altura = True
        print('\n')
    except:
        print("Erro na entrada de dados, por favor ultilize somente numeros e use '.' no lugar da Virgula")

valid_peso = False
while valid_peso == False:
    peso = input('Digite seu peso: ')
    try:
        peso = float(peso)
        valid_peso = True
        print('\n')
    except:
        print("Erro na entrada de dados, por favor ultilize somente numeros e use '.' no lugar da Virgula")

v_imc = str(IMC(peso,altura))
c_imc = class_imc(sexo,peso,altura)

print('O seu IMC é:',v_imc[0:5])
print('A sua classificação é:',c_imc)