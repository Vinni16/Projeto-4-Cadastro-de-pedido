pedido = []


#Funções do programa

def aplicacao():
	escolha1 = input('Deseja fazer seu pedido agora? ')
	if escolha1 == 'sim':
		lanches()
	if escolha1 == 'nao':
		print('Ok, aguardo sua escolha')
		aplicacao()

def lanches():
	print('''Menu de Lanches:
		1 - X-Tudo
		2 - X-Bacon
		3 - X-Egg
	''')
	choose1 = input('Escolha seu lanche das opções acima: ')
	if choose1 == '1':
		print('Você escolheu opção: 1 - X-Tudo')
		print('Agora, escolha sua bebida: ')
		bebidas()
	if choose1 == '2':
		print('Você escolheu opção: 1 - X-Bacon')
		print('Agora, escolha sua bebida: ')
		bebidas()
	if choose1 == '3':
		print('Você escolheu opção: 1 - X-Egg')
		print('Agora, escolha sua bebida: ')
		bebidas()

def bebidas():
	print('''
		1 - Coca-Cola
		2 - Guaraná
		3 - Fanta Uva
	''')
	choose2 = input('Digite aqui: ')
	if choose2 == '1':
		print('Você escolheu a bebida Coca-cola.')
	if choose2 == '2':
		print('Você escolheu a bebida Guaraná.')
	if choose2 == '3':
		print('Você escolheu a bebida Fanta Uva.')


#Inicio do programa
print('Bem vindo de volta!')
aplicacao()