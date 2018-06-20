#RECONOCIMIENTO CADENAS TERMINACION 01
import threading
import random
from tkinter import*

archivo = open("Datos5.txt", "w")

cadena = []
rutaseguida = []
auxacept = 0

#Estados
def q0(cad1):
	x = 0
	#3.-
	#Recorremos cada caracter de la cadena
	for i in cad1:
		#Verificamos que no esté en el último caracter
		if x+1 < len(cad1):
			#Esto pasa haya 0's o 1's
			rutaseguida.append("q0")
			print ("q0: " + cad1[x:])
			archivo.write("q0: " + cad1[x:] + "\n")
		#Si se recibe un '0', se manda comienza un hilo para el estado q1
		if i == '0':
			h1 = threading.Thread(target = q1, args = (cad1[x+1:],))
			h1.start()
			h1.join()
		#Vamos recorriendo cada una de los caracteres
		x+=1	
	#la cadena no puede medir 1
	if len(cad1) == 1:
		print ("Rechazada")
		rutaseguida.append("q0")
	if len(cad1) == 2:
		if cad1 != '01':
			print ("Rechazada")

def q1(cad2):
	if len(cad2) > 0:
		print ("	q1: " + cad2)
		archivo.write("		q1: " + cad2 + "\n")
		if cad2[0] == '1':
			rutaseguida.append("q1")
			h1 = threading.Thread(target = q2, args = (cad2[0:],))
			h1.start()
			h1.join()
		else:
			print ("		Rechazada \n")
			archivo.write("		Rechazada \n")
			auxacept = 1

def q2(cad3):
	if len(cad3) > 0:
		print ("		q2: " + cad3)
		archivo.write("		q2: " + cad3 + "\n")
		#Verificamos que sea el ultimo caracter
		if len(cad3) == 1:
			#Si es el ultimo caracter y termina en uno (predecido de un 0) pasa al estado de aceptado (res)
			if cad3[0] == '1':
				rutaseguida.append("q2")
				res()
		else:
			rutaseguida.pop()
			print ("		Rechazada \n")
			archivo.write("		Rechazada \n")
			auxacept = 2

def res():
	print ("\nCadena Aceptada.")
	archivo.write("\nCadena Aceptada.\n")
	auxacept = 3
	print(auxacept)
	print ("Camino de la ruta aceptada: ", str(rutaseguida))
	archivo.write("Camino de la ruta aceptada: " + str(rutaseguida))

######

#Programa principal
aux = input ("Bienvenido al automata de reconocimiento de cadenas terminadas en '01'. \n ¿Qué modo desea utilizar? Manual(1) o Aleatorio(2) \n ")
#1.- Creacion de cadena a evaluar
if int(aux) == 1:
	cadena = input ("Ingresa tu cadena: ")
	print ("Cadena ingresada: '" + cadena + "'\n")
else:
	rand = random.randrange(10000)
	cadena = str(bin(rand)[2:])
	print ("Cadena generada:'" + str(cadena) + "'\n")

archivo.write("Probando la cadena '"+ cadena +"'\n\n")

#2.- Mandamos en un hilo la cadena a la función q0
h1 = threading.Thread(target = q0, args = (cadena,)) 

h1.start()
h1.join()



##############

#Gráficos

ventana = Tk()
canv = Canvas(ventana,width=800,height=300)
ventana.geometry("800x300")

ventana.title('Automata Paridad')

p= Label(ventana,text="Cadena a verificar. \n Cadena:"+cadena).place(x=10,y=10)

#q0
p0= Label(ventana,text="q0").place(x=55,y=105)

if rutaseguida[-1] == "q0":
	canv.create_oval(20,70,110,160, fill="red")
else:	
	canv.create_oval(20,70,110,160, fill="blue")


canv.create_oval(35,85,95,145)
n1= Label(ventana,text="0").place(x=190,y=35)
canv.create_oval(70,155,80,165, fill="black")
n2= Label(ventana,text="0,1").place(x=65,y=185)

#q1
p1= Label(ventana,text="q1").place(x=305,y=105)

if rutaseguida[-1] == "q1":
	canv.create_oval(270,70,360,160, fill="red")
else:
	canv.create_oval(270,70,360,160, fill="blue")

canv.create_oval(280,75,290,85, fill="black")
n1= Label(ventana,text="1").place(x=450,y=35)

#q2
p2= Label(ventana,text="q2").place(x=565,y=105)

if rutaseguida[-1] == "q2":
	canv.create_oval(530,70,620,160, fill="green")
else:
	canv.create_oval(530,70,620,160, fill="blue")
canv.create_oval(540,75,550,85, fill="black")


#lineas
#0-1
xy1 = 95, 60, 286, 105
canv.create_arc(xy1, start=0, extent=180, style="arc")

#3-1
xy7 = 56, 160, 86, 180
canv.create_arc(xy7, start=90, extent=330, style="arc")

#0-1
xy1 = 345, 60, 546, 105
canv.create_arc(xy1, start=0, extent=180, style="arc")



canv.place(x=0,y=0)
ventana.mainloop()