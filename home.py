#Funções do programa

def aplicacao():
	escolha1 = input('Deseja fazer seu pedido agora? ')
	if escolha1 == 'sim':
		lanches()
	if escolha1 == 'nao':
		print('Ok, aguardo sua escolha')
		app()

def lanches():
	print('''Menu de Lanches:
		1 - X-Tudo
		2 - X-Bacon
		3 - X-Egg
	''')
	choose1 = input('Escolha seu lanche das opções acima: ')
	if choose1 == '1':
		print('Você escolheu opção: 1 - X-Tudo')
	if choose1 == '2':
		print('Você escolheu opção: 1 - X-Bacon')
	if choose1 == '3':
		print('Você escolheu opção: 1 - X-Egg')

def bebidas():
	print('''
		1 - Coca-Cola
		2 - Guaraná
		3 - Fanta Uva
	''')


#Inicio do programa
print('Bem vindo de volta!')
aplicacao()