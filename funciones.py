#esta funcion eligira un numero al azar "el ganador"

import random

def ruleta():
	
	n_ruleta=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,
	14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,
	30,31,32,33,34,35,36]

	n_ganador = int (random.choice(n_ruleta))

	if (n_ganador != 0):
		if ( n_ganador % 2 == 0 ):
 			print ( str(n_ganador) + " es par")

		else:
 			print (str(n_ganador)+" es impar")

 	else:

 		print n_ganador


ruleta()
