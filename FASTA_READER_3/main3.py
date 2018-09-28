import sys
import gzip
Aminoacidos= {'I':'ATH', 'M':'ATG', 'T':'ACN', 'N':'AAY', 'K':'AAR', 'S':'WSN', 'R':'MGN',
                  'L':'YTN', 'P':'CCN', 'H':'CAY', 'Q':'CAR', 'V':'GTN', 'A':'GCN', 'D':'GAY',
                  'E':'GAR', 'G':'GGN', 'F':'TTY', 'Y':'TAY', 'X':'TRR', 'C':'TGY', 'W':'TGG' , 'U':'U'} 
if (len(sys.argv)>2 or len(sys.argv)<2):
	print ('Numero de argumentos invalidos')
else:
	adn= ''
	e = 0
	fileadn = gzip.open(sys.argv[1])
	for linea  in  fileadn:
		linea=linea.decode()
		if (('>') == (linea[0])):
			print("\n\n")
			print (linea)
		else:
			linea=linea.replace('\n','')
			for i in linea:
				adn += Aminoacidos[i]
			print (adn)
			adn=''


