#EXPRESION REGURAL A AUTOMATA
import sys
import time
import random
sys.setrecursionlimit(1000)
from tkinter import*

archivo = open("Datos8.txt", "w")

expresiones = []

print ("Generador de cadenas de la expresión: (0 U 10)*(e U 1)")	
archivo.write("\n"+"Generador de cadenas de la expresión: (0 U 10)*(e U 1)")

for i in range(0,10):
	print(i+1,".-")
	archivo.write("\n"+str(i+1)+".-")
	expresiones.append("")

	ck = random.choice(["", "n"]) #random para cerradura de kleene para ver si es e o n
	print ("ck=",ck)
	archivo.write("\n"+"ck="+ck)

	if ck == "n":
		n = random.randint(1, 10)#si es n otro random para encontrar ese n
		print("n:",n)
		archivo.write("\n"+"n:"+str(n))
		for j in range(0,n):
			a1 = random.choice(["0", "10"]) #random para ver si se escoje 0 o 10
			print("a1=",a1)
			archivo.write("\n"+"a1="+a1)
			expresiones[i] = expresiones[i]+a1



	print ("Expresion antes de la multiplicacion:",expresiones[i])
	archivo.write("\n"+"Expresion antes de la multiplicacion:"+expresiones[i])

	a2 = random.choice(["", "1"])#random para escoger entre e o 1
	print("a2="+a2)
	archivo.write("\n"+"a2="+a2)


	if(a2=="1"):
		print("Hay 1 al final, se suma")
		archivo.write("\n"+"Hay 1 al final, se suma")
		expresiones[i] = expresiones[i]+a2 	

	print (expresiones[i], "\n")
	archivo.write("\n"+expresiones[i]+ "\n")

print (expresiones)
archivo.write("\n"+str(expresiones))