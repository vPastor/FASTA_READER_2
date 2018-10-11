import sys
import gzip
#Diccionario de los aminoacidos
Aminoacidos= {'I':'ATH', 'M':'ATG', 'T':'ACN', 'N':'AAY', 'K':'AAR', 'S':'WSN', 'R':'MGN',
                  'L':'YTN', 'P':'CCN', 'H':'CAY', 'Q':'CAR', 'V':'GTN', 'A':'GCN', 'D':'GAY',
                  'E':'GAR', 'G':'GGN', 'F':'TTY', 'Y':'TAY', 'X':'TRR', 'C':'TGY', 'W':'TGG' , 'U':'U'} 
#si pasan menos o mas de 2 argumentos, corrección de errores
if (len(sys.argv)>2 or len(sys.argv)<2):
	print ('Numero de argumentos invalidos')
else:
	#inicializamos la variable adn para ir introduciendo datos en ella
	adn= ''
	e = 0
	fileadn = gzip.open(sys.argv[1])
	for linea  in  fileadn:
		linea=linea.decode()
		#si al principio de la linea encuentra el signo >, es que es una cabecera, por lo tanto, imprimir la cabecera
		if (('>') == (linea[0])):
			print("\n\n")
			print (linea)
		else:
			#si no, caracter por caracter va buscando el caracter en el diccionario y va introduciendo los tripletes, y los va imprimiendo
			linea=linea.strip()
			for i in linea:
				adn += Aminoacidos[i]
			print (adn)
			adn=''


