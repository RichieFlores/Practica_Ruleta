#esta funcion eligira un numero al azar "el ganador"

import random

def ruleta():
	
	n_ruleta=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,
	14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,
	30,31,32,33,34,35,36]

	n_ganador = int (random.choice(n_ruleta))

	if (n_ganador != 0):
		if ( n_ganador % 2 == 0 ):
 			return ( str(n_ganador) + " es par")

		else:
 			return (str(n_ganador)+" es impar")

 	else:

 		return n_ganador




def apuesta():

	flag=1
	n_apuesta=[]
	c_apuesta=[]

	while flag ==1:
	#n_apuesta solo se usa para que el usuario ingrese las apuestas 
		
		n_apuesta.append (raw_input("Ingresa un  numero al que le quieres apostar: "))
		c_apuesta.append (raw_input ("Ingresa el monto que deseas apostar: "))

		mas_apuestas=raw_input("Deseas hacer otra apuesta? Si o No")
		

		if mas_apuestas.upper() == "NO":
			flag =0


	return n_apuesta











	



	

