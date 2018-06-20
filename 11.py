#ARBOL DE DERIVACIONES
ar = open("Datos11.txt", "w")

from random import randint
print("Bienvenido al arbol de Derivaciones:")
op = input("¿Qué modo desea utilizar? 1)Manual 2)Automático")

if op == "1":
	print("Modo manual, ingrese una cadena compuesta por '(' y ')'")
	cad = input() #cadena a evaluar
	ar.write(cad)

else:
	print("Modo automático")
	ar.write("\n"+"Modo automático")
	cad=""
	largo=randint(1,4)#rand()%1001
	for i in range(0,largo+1):
		rand1=randint(0,1)
		if(rand1==1):
			cad=cad+')'
		else:
			cad=cad+'('
	print(cad)
	ar.write("\n"+cad)

final = "B" 
resultado = ""
print("")
ar.write("\n"+"")

longitud = len(cad)
print("B")
ar.write("\n"+"B")

for i in range(0,longitud):
	#print(i)
	if(final[0] == "B"):

		if (cad[i] == "("):
			final = "R"+final
			resultado = resultado + "("
			print (resultado+final)
			ar.write("\n"+resultado+final)
			continue

		if(cad[i] == ")"):
			print("Condicion de derivacion no válida")
			ar.write("\n"+"Condición de derivación no válida")
			final =final+"X"
			break

	if(final[0] == "R"):

		if(cad[i]=="("):
			final = "R"+final
			resultado = resultado +"("
			print (resultado+final)
			ar.write("\n"+resultado+final)
			continue

		if(cad[i]==")"):
			final = final[1:len(final)]
			resultado = resultado + ")"
			print (resultado+final)
			ar.write("\n"+resultado+final)
			continue

if(final=="B"):
	print("\n"+resultado)
	print("\nEstá balanceada")
	ar.write("\n"+"\n"+resultado)
	ar.write("\n"+"\nEstá balanceada")

if(final!="B"):
	print("\nNo está balanceada")
	ar.write("\n"+"\nNo está balanceada")
	
	
