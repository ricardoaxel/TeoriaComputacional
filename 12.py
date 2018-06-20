#MAQUINA DE TURING

import sys
import time
ar = open("Datos12.txt", "w")
import random
from tkinter import*
from random import randint
arc = open("Datos12.txt", "w")


print("MAQUINA DE TURING:")
op = input("¿Qué modo desea utilizar? 1)Manual 2)Automático\n")
if op == "1":
	cadena = input("Ingrese la cadena deseada: ")
else:
	rand = random.randrange(10000)
	cadena = str(bin(rand)[2:])
	print ("Cadena generada: ",cadena)
cad = []
for x in cadena:
	cad.append(x)

arc.write(str(cad))
print ("\n")




#Declaracion interfaz grafica------
ventana = Tk()
canv = Canvas(ventana,width=1200,height=600)
ventana.geometry("1200x600")
#
canv.pack() 
xspeed=5
yspeed=0
tk= Tk()
e = "a" #a son 0's b son 1's
aux1 = 0 #auxiliar para ver los 1 que se van llenando
cuenta = 0
o= Label(ventana,text="Cadena a verificar. \n Cadena:"+str(cad)).place(x=10,y=10)

cuad= (len(cad)*50)/2 #Tamaño inicial de nuestra barra
#canv.create_rectangle(50, 500, 1150, 550, width=0, fill='black')
 #posicion auxiliar para los cuadritos




#------------------------
try:
	estado = "q0" #estado inicial
	i=0 #Lleva el índice de nuestra cadena
	while(estado != "q5"): #Analizando toda la cinta
		pos=0
		posaux=0
		for x in cad:
			posicua = 600-50*(pos/2)#posicion inidel cuadrito actual
			canv.create_rectangle(600-(len(cad)/2)*50+pos*50, 500, 650-(len(cad)/2)*50+pos*50, 550, width=1, fill='green')
			if(pos==i):
				canv.create_rectangle(600-(len(cad)/2)*50+pos*50, 500, 650-(len(cad)/2)*50+pos*50, 550, width=1, fill='blue')
			pos = pos+1

		u= Label(ventana,text=cad).place(x=600,y=450)
		tk.update()
		time.sleep(1.5)
		
		print(i)
		print(len(cad))
		if(i==-1):
			cad.insert(0,"")
			i=0
		if(estado=="q0"): #Condiciones q0
				
			if(cad[i]=="0"):
				estado = "q0"
				cad[i] = "0"
				i= i+1
				print("(q0,0,R)")
				print(cad)
				arc.write("(q0,0,R)\n"+str(cad)+"\n")
				o= Label(ventana,text="(q0,0,R)").place(x=600,y=350)
					

			elif(cad[i]=="1"):
				estado = "q1"
				cad[i] = "1"
				i=i+1
				print("(q1,1,R)")
				print(cad)
				arc.write("(q1,1,R)\n"+str(cad)+"\n")
				o= Label(ventana,text="(q1,1,R)").place(x=600,y=350)
					

			elif(cad[i]==""):
				cad[i]="0"
				estado = "q3"
				i=i-1
				print("(q3,0,L)")
				print(cad)
				arc.write("(q3,0,L)\n"+str(cad)+"\n")
				o= Label(ventana,text="(q3,0,L)").place(x=600,y=350)



		if(estado=="q1"): #Condiciones q1

			if(cad[i]=="0"):
				estado = "q0"
				cad[i] = "1"
				i= i+1
				print("(q0,1,R)")
				print(cad)
				arc.write("(q0,1,R)\n"+str(cad)+"\n")
				o= Label(ventana,text="(q0,1,R)").place(x=600,y=350)

			elif(cad[i]=="1"):
				estado = "q2"
				cad[i] = "1"
				i= i+1
				print("(q2,1,R)")
				print(cad)
				arc.write("(q2,1,R)\n"+str(cad)+"\n")
				o= Label(ventana,text="(q2,1,R)").place(x=600,y=350)

			elif(i==len(cad)-1):
				print("Cadena no aceptada")
				break


		if(estado=="q2"): #Condiciones q2

			if(cad[i]=="0"):
				estado = "q0"
				cad[i] = "1"
				i= i+1
				print("(q0,1,R)")
				print(cad)
				arc.write("(q0,1,R)\n"+str(cad)+"\n")
				o= Label(ventana,text="(q0,1,R)").place(x=600,y=350)

			elif(cad[i]=="1"):
				estado = "q2"
				cad[i] = "0"
				i= i+1
				print("(q2,0,R)")
				print(cad)
				arc.write("(q2,0,R)\n"+str(cad)+"\n")
				o= Label(ventana,text="(q2,0,R)").place(x=600,y=350)

			elif(i==len(cad)-1):
				print("Cadena no aceptada")
				break



		if(estado=="q3"): #Condiciones q3
			if(cad[i]=="0"):
				estado = "q3"
				cad[i] = "0"
				i= i-1
				print("(q3,0,L)")
				print(cad)
				arc.write("(q3,0,L)\n"+str(cad)+"\n")
				o= Label(ventana,text="(q3,0,L)").place(x=600,y=350)


			elif(cad[i]=="1"):
				estado = "q3"
				cad[i] = "1"
				i= i-1
				print("(q3,1,L)")
				print(cad)
				arc.write("(q3,1,L)\n"+str(cad)+"\n")
				o= Label(ventana,text="(q3,1,L)").place(x=600,y=350)

			elif(cad[i]==""):
				cad[i]="0"
				estado = "q0"
				i= i+1
				print("(q0,0,R)")
				print(cad)
				arc.write("(q0,0,R)\n"+str(cad)+"\n")
				o= Label(ventana,text="(q0,0,R)").place(x=600,y=350)

		if(i==len(cad)):
			cad.append("")

		posaux=posaux+1

	canv.place(x=0,y=0)
	ventana.mainloop()
except:
	print("Cadena no aceptada")


