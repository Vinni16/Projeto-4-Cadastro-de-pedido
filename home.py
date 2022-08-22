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
		choose1 = 0
		print('Você escolheu opção: 1 - X-Tudo')
		pedido.append(OpcoesDeLanches.get(1))
		print('Agora, escolha sua bebida: ')
		bebidas()

	if choose1 == '2':
		print('Você escolheu opção: 1 - X-Bacon')
		pedido.append(OpcoesDeLanches.get(2))
		print('Agora, escolha sua bebida: ')
		bebidas()

	if choose1 == '3':
		print('Você escolheu opção: 1 - X-Egg')
		pedido.append(OpcoesDeLanches.get(3))
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
		pedido.append(OpcoesDeBebidas.get(1))
		print("Aqui está seu pedido")
		print(pedido)

	if choose2 == '2':
		print('Você escolheu a bebida Guaraná.')
		pedido.append(OpcoesDeBebidas.get(2))
		print("Aqui está seu pedido")
		print(pedido)

	if choose2 == '3':
		print('Você escolheu a bebida Fanta Uva.')
		pedido.append(OpcoesDeBebidas.get(3))
		print("Aqui está seu pedido")
		print(pedido)


#Inicio do programa

print('Bem vindo de volta!')
pedido = []
OpcoesDeLanches = {1 : "X-Tudo", 2 : "X-Bacon", 3 : "X-Egg"}
OpcoesDeBebidas = {1 : "Coca-cola", 2 : "Guaraná", 3 : "Fanta Uva"}
aplicacao()