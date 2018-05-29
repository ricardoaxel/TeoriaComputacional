import random

#NUMEROS PRIMOS

# Abre archivo para escribir
archivo = open('datos2.txt','w')


print ("Numeros primos. \n")
opc = input("Que desea hacer\n 1)Ingresar maximo \n 2)Generar maximo \n")

if (opc =="1"):
	n = int(input("Ingrese un maximo:\n "))
else: 
	n = random.randrange(10000)


aux1 = n*.75
aux2 = n*.5
aux3 = n*.25

print ("Encontrando numeros primos entre 2 y",n,"...")

archivo.write ("{")
while n>1:	

	a=0

	for i in range(1,n+1): #1-3
		if(n%i==0): # 3%1 = 0, 3%2 = 1, 3%3 = 0
	 		a=a+1   # a = 1,   a = 1,  a = 2

	if(a==2):
		archivo.write (str(n))

		if(n != 2):
			archivo.write (",")
	n = n-1

	if n == (aux1):
		print ("...25%")

	if n == (aux2):
		print ("...50%")

	if n == (aux3):
		print ("...75%")

archivo.write ("}")
archivo.close
print ("Archivo generado (datos2.txt)")