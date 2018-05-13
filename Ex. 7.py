print('Inicio do programa')
print()

x = 's'
total = 0
valid_preco = False
fatura = []

while x == 's':
    produto = input('Digite o nome do produto: ')
    while valid_preco == False:
        preco = (input('Digite o valor do produto: '))
        try:
            preco = float(preco)
            if preco <= 0:
                print('O preco precisa ser maior que Zero')
            else:
                valid_preco = True
        except:
            print('Formado de texto inválido.')
    fatura.append([produto,preco])
    total += preco
    valid_preco = False
    x = input('Deseja continuar a compra?').lower()

for i in fatura:
    print(i[0],'-',i[1],'R$')

print('O Total da fatura é: {:.2f}R$'.format(total))
