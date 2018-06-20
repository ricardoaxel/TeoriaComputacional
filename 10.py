#GENERADOR DE PALINDROMOS
ar = open("Datos10.txt", "w")
import random
from random import randint

print("Generador de palindromos")
op = input("1)Longitud manual o 2)Generar un palíndromo de longitud aleatoria ")

if op == "1":
	lon = int(input("Ingrese la longitud deseada:"))
else:
	lon = randint(0,1000)

ar.write("Longitud: "+str(lon)+"\n")
l = int(lon/2)
if(lon%2!=0):
	print ("inpar")
	inpar=1
else:
	inpar=0

palin = "P" #palíndromo generado

for i in range(0,l+1):
	if i == l:
		final =palin.split()

		if inpar == 0:
			print ("Se aplicó la regla 1 (P -> e)")
			final.remove("P")
			print (final)
			ar.write(str(final)+"\n")

		if inpar == 1:
			reglas1 = randint(2,3)
			if reglas1 == 2:
				print ("Se aplicó la regla 2 (P -> 0)")
				final[l] = "0"
				print (final)
				ar.write(str(final)+"\n")
			if reglas1 == 3:
				print ("Se aplicó la regla 3 (P -> 1)")
				final[l] = "1"
				print (final)
				ar.write(str(final)+"\n")

	else:
		reglas2 = randint(4,5)
		if reglas2 == 4:
			print ("Se aplicó regla 4 (P -> 0P0)")
			palin = "0 "+palin+" 0"
			print (palin)
			ar.write(str(palin)+"\n")

		if reglas2 == 5:
			print("Se aplicó regla 5 (P -> 1P1)")
			palin = "1 "+palin+" 1"
			print(palin)
			ar.write(str(palin)+"\n")

	print("\n")
