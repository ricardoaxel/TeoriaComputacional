import random

# Abre archivo para escribir
archivo = open('datos1.txt','w')

print ("Combinaciones de 1 y 0. \n")
opc = input("Que desea hacer\n 1)Ingresar una potencia \n 2)Generar potencia \n")

if (opc =="1"):
	potencia = int(input("Ingrese una potencia:\n "))
else: 
	potencia = random.randrange(100)



print ("Potencia elegida:", potencia, "\nSe generara un archivo con:  combinaciones...")

archivo.write("{")


for x in range(0,potencia): 

	numcom = 2 ** potencia #numero de combinaciones
	auxpot = potencia

	while numcom > 0:

		if numcom != 2**potencia:

			archivo.write(str(bin(numcom)[2:potencia+2]).zfill(potencia))
			archivo.write (",")
		
		numcom = numcom - 1

		if numcom == 0: #para imprimir la combinación final (o*p)
			while auxpot > 0:
				archivo.write("0")
				auxpot = auxpot - 1

	potencia = potencia - 1 #para ir bajando de potencia

	if (potencia != 0): #Validacion para que no aparezca "," al final
		archivo.write(",")

	

	
archivo.write("}")
archivo.close
print ("Listo")