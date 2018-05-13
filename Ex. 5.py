cores = {'verde':'green','vermelho':'red','preto':'black','branco':'white'}
cor = input('Escolha a cor que deseja Traduzir: ').lower()

traducao = cores.get(cor, 'Esta cor não consta no meu dicionario.')
print (traducao)

print()
input('Aperte enter para sair')