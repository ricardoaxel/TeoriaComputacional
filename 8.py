#EXPRESION REGURAL A AUTOMATA

import sys
import time
import random
sys.setrecursionlimit(1000)
from tkinter import*

expresiones = []

for i in range(0,10):
	print(i+1,".-")
	expresiones.append("")

	ck = random.choice(["e", "n"]) #random para cerradura de kleene para ver si es e o n
	print ("ck=",ck)

	if ck == "n":
		n = random.randint(1, 10)#si es n otro random para encontrar ese n
		print("n:",n)
		for j in range(0,n):
			a1 = random.choice(["0", "10"]) #random para ver si se escoje 0 o 10
			print("a1=",a1)
			expresiones[i] = expresiones[i]+a1

	print ("EXPRESION REGURAL A AUTOMATA:")	
	print ("Expresion antes de la multiplicacion:",expresiones[i])
	a2 = random.choice(["e", "1"])#random para escoger entre e o 1
	print("a2=",a2)


	if(a2 =="e"): #verificamos que si hay algo que este sucedido de una 'e', termine solo como 'e'
		print("Hay e al final, se queda sólo e")
		expresiones[i] = "e"

	if(a2=="1"):
		print("Hay 1 al final, se suma")
		expresiones[i] = expresiones[i]+a2 	



	print (expresiones[i], "\n")

print (expresiones)