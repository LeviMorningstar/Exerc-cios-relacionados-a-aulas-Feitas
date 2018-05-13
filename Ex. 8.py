print('Inicio do programa, Este programa Calcula o seu IMC.')
print()

valid_sexo = False
valid_peso = False
valid_altura = False

lista_sexo_m = ['m','masculino','homem']
lista_sexo_f = ['f','feminino','mulher']
x = ('s')
s = ('s','sim','pode cre','aham é noix','pode pa')
while x in s:
    while valid_sexo == False:
        sexo = input('Digite o Seu sexo, M para masculino ou F para feminino: ').lower()
        if sexo not in lista_sexo_m and sexo not in lista_sexo_f:
            print('Erro na entrada de dados, por favor Ultilize um formato valido.')
        else:
            valid_sexo = True

    while valid_altura == False:
        altura = input('Digite sua Altura: ')
        try:
            altura = float(altura)
            valid_altura = True
        except:
            print("Erro na entrada de dados, por favor ultilize somente numeros e use '.' no lugar da Virgula")

    while valid_peso == False:
        peso = input('Digite seu peso: ')
        try:
            peso = float(peso)
            valid_peso = True
        except:
            print("Erro na entrada de dados, por favor ultilize somente numeros e use '.' no lugar da Virgula")

    IMC = peso / (altura*altura)


    if sexo in lista_sexo_m:
        print(sexo)
        if IMC < 20.7:
            print('Abaixo do peso.')
        elif IMC >= 20.7 and IMC <= 26.4:
            print('No peso Normal.')
        elif IMC > 26.4 and IMC <= 27.8:
            print('Marginalmente aceima do Peso.')
        elif IMC > 27.8 and IMC <= 31.1:
            print('Acima do peso Ideal.')
        else:
            print('Obeso.')
    elif sexo in lista_sexo_f:
        print(sexo)
        if IMC < 19.1:
            print('Abaixo do peso.')
        elif IMC >= 19.1 and IMC <= 25.8:
            print('No peso Normal.')
        elif IMC > 25.8 and IMC <= 27.3:
            print('Marginalmente aceima do Peso.')
        elif IMC > 27.3 and IMC <= 32.3:
            print('Acima do peso Ideal.')
        else:
            print('Obeso.')
    else:
        print('Erro.')

    valid_sexo = False
    valid_peso = False
    valid_altura = False

    x = input('Deseja continuar?')