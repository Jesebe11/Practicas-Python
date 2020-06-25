lista_palabras = dict()

whileTrue: decision = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

Bienvenido al traductor. ¿Qué deseas hacer?

	[A]gregar palabra
	[V]er diccionario
	[S]alir

--- * --- Digite la opción que desea realizar: '''))

print('')

if decision  == 'A'or decision =='a':

			palabra_esp = str(input('Escriba la palabra en español: '))
			palabra_eng = str(input('Escriba la palabra en ingles: '))
			print('')


			# if palabra_esp == '' or  palabra_eng == '' :
			# 	print('Alguna palabra quedó vacía')
			# 	# break
			# else:

			dict_temp = {palabra_esp : palabra_eng}
			lista_palabras.update(dict_temp)

			print('Palabra añadida correctamente')
			print('')

elif decision == 'V'or decision == 'v':

			print('El diccionario contiene las siguientes palabras: ')
			print('')
			# print(lista_palabras)

			contador = 0;
			for key in lista_palabras.keys():
				contador += 1
				print('# {} {} - {}'.format(contador,key,lista_palabras[key]))

			print('')

elif decision == 'S'or decision == 's':
     break

else:
     print('La opcion digitada no es valida')

print('')