import sys
import gzip
#diccionario de aminoacidos
traduce = {
	'AAA': 'K','AAG': 'K','AAT': 'N','AAC': 'N',
	'AGA': 'R','AGG': 'R','AGT': 'S','AGC': 'S',
	'ATA': 'I','ATG': 'M','ATT': 'I','ATC': 'I',
	'ACA': 'T','ACG': 'T','ACT': 'T','ACC': 'T',
	'GAA': 'E','GAG': 'E','GAT': 'D','GAC': 'D',
	'GGA': 'G','GGG': 'G','GGT': 'G','GGC': 'G',
	'GTA': 'V','GTG': 'V','GTT': 'V','GTC': 'V',
	'GCA': 'A','GCG': 'A','GCT': 'A','GCC': 'A',
	'TAA': '-','TAG': '-','TAT': 'Y','TAC': 'Y',
	'TGA': '-','TGG': 'W','TGT': 'W','TGC': 'W',
	'TTA': 'L','TTG': 'L','TTT': 'F','TTC': 'F',
	'TCA': 'S','TCG': 'S','TCT': 'S','TCC': 'S',
	'CAA': 'Q','CAG': 'Q','CAT': 'H','CAC': 'H',
	'CGA': 'R','CGG': 'R','CGT': 'R','CGC': 'R',
	'CTA': 'L','CTG': 'L','CTT': 'L','CTC': 'L',
	'CCA': 'P','CCG': 'P','CCT': 'P','CCC': 'P',
	}
#si hay mas o menos de 2 argumentos, mostrar mensaje informativo
if (len(sys.argv)>2 or len(sys.argv)<2):
	print ('Numero de argumentos invalidos')
else:
	proteina= ''
	e = 0
	#vamos leyendo el documento introducido
	fileadn = gzip.open(sys.argv[1])
	for linea  in  fileadn:
		linea=linea.decode()
		#imprime cabecera
		if (('>') == (linea[0])):
			print (linea)
		else:
			#imprime y traduce los tripletes a aminoacidos
			linea=linea.replace('\n','')
			if len(linea) % 3 == 0:
				for i in range(0, len(linea), 3):
					triplete = linea[i: i + 3]
					proteina += traduce[triplete]
					print (proteina)


