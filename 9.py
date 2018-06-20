#AUTOMATA DE PILA
import sys
import time
import random
sys.setrecursionlimit(1000)
from tkinter import*

archivo = open("Datos9.txt", "w")

class Pila(object):
	
	def __init__(self):
		super(Pila, self).__init__()
		self.arreglo = []
		self.cnt = 0

	def push(self, objeto):
		self.cnt += 1
		self.arreglo.append(objeto)
	def pop(self):
		if self.cnt == 0:
			return False
		else:
			self.cnt -= 1
			del self.arreglo[self.cnt]
			return True
	def top(self):
		return self.arreglo[self.cnt-1]



print("Cadenas numero par de 1 y 0 \n 1)Modo manual. 2)Modo automatico")
archivo.write("Cadenas numero par de 1 y 0 \n 1)Modo manual. 2)Modo automatico")
opc = input()

if (opc=="1"):
	cad = input("Cadena a evaluar:\n") #cadena a evaluar
	archivo.write("Cadena a evaluar: \n")

else:
	rand = random.randrange(10000)
	cad = str(bin(rand)[2:])
	print("Cadena generada:", cad)
	archivo.write("\n Cadena generada:"+cad)
cadc = cad[::-1] #cadena invertida para meterla a la pila

p = Pila()



#Declaracion interfaz grafica
ventana = Tk()
canv = Canvas(ventana,width=800,height=600)
ventana.geometry("800x600")


#
canv.pack() 
xspeed=5
yspeed=0
tk= Tk()

e = "a" #a son 0's b son 1's
aux1 = 0 #auxiliar para ver los 1 que se van llenando

cuenta = 0

o= Label(ventana,text="Cadena a verificar. \n Cadena:"+cad).place(x=10,y=10)

cont = 0

conta = 0 #auxiliar para contabilizar los 0 que llegan adecuadamente
contb = 0 #auxiliar para contabilizar los 1 que llegan adecuadamente
conterr = 0 #auxiliar para contar los errores

canv.create_rectangle(300, 50, 400, 550, width=0, fill='black')


for i in cadc:
	

	u= Label(ventana,text="Cadena evaluandose \n "+cad[0:len(cad)-cont]).place(x=10,y=100)
	tk.update()
	time.sleep(.5)
	cont = cont + 1

	if(cadc[cuenta]=="1"):
		cuenta = cuenta + 1
		p.push("X")
		print(p.arreglo)
		archivo.write("\n"+str(p.arreglo))
		aux1= aux1+1
		e = "c"

		#grafico
		canv.create_rectangle(300, 500-conterr*25, 400, 550-conterr*25, width=1, fill='red', outline='white')
		conterr= conterr+1
		time.sleep(.5)
		conterr = conterr + 1	
		continue

	if(i=="0" and e == "a"):

		p.push(i)
		print(p.arreglo)
		archivo.write("\n"+str(p.arreglo))
		#grafico
		canv.create_rectangle(300, 500-conta*25, 400, 550-conta*25, width=1, fill='blue', outline='white')
		conta= conta+1
		time.sleep(.5)
		conta = conta + 1
		continue

	if(i=="0" and e == "b"): #el estado c sirve cuando se comienza con un 1 y sólo se van añadiendo X's cuando pasan nuevos 1, cuando pasa un 0 no pasa nada
		e = "c"
		p.push("X")
		print(p.arreglo)
		archivo.write("\n"+str(p.arreglo))
		continue

	if(i=="0" and e == "c"):
		p.push("X")
		print(p.arreglo)
		archivo.write("\n"+str(p.arreglo))

		continue

	if(i=="1" and e =="c"):
		p.push("X")
		print(p.arreglo)
		archivo.write("\n"+str(p.arreglo))

		canv.create_rectangle(300, 500-conterr*25, 400, 550-conterr*25, width=1, fill='red', outline='white')
		conterr= conterr+1
		time.sleep(.5)
		conterr = conterr + 1	
		continue

	if(i=="1" and e=="a"):
		e="b"
		p.pop()
		print(p.arreglo)
		archivo.write("\n"+str(p.arreglo))
		aux1= aux1+1

		#grafico
		canv.create_rectangle(300, 550-((conta)*25), 400, 600-(conta)*25, width=1, fill='black', outline='white')
		contb= contb+1
		time.sleep(.5)
		continue

	if(i=="1" and len(p.arreglo)<aux1):
		p.push("X")
		print(p.arreglo)
		archivo.write("\n"+str(p.arreglo))
		aux1= aux1+1

		#grafico
		canv.create_rectangle(300, 500-conterr*25, 400, 550-conterr*25, width=1, fill='red', outline='white')
		conterr= conterr+1
		time.sleep(.5)
		conterr = conterr + 1
		continue

	if(i=="1" and e=="b"):
		p.pop()
		print(p.arreglo)
		archivo.write("\n"+str(p.arreglo))


		#grafico
		canv.create_rectangle(300, 550-((conta)*25)+contb*50, 400, 600-(conta)*25+contb*50, width=1, fill='black', outline='white')
		time.sleep(.5)
		contb = contb + 1	
		continue

	print("\n"+str(p.arreglo))
	archivo.write("\n"+str(p.arreglo))

a=len(p.arreglo)
if(a==0):
	print("Cadena válida")
	archivo.write("\nCadena válida")
	o= Label(ventana,text="Cadena VALIDA :D!").place(x=500,y=300)
	canv.create_rectangle(300, 50, 400, 550, width=0, fill='green')

else:
	print("Cadena inválida")
	archivo.write("\nCadena inválida")
	o= Label(ventana,text="Cadena INVALIDA :(").place(x=500,y=300)
	canv.create_rectangle(300, 50, 400, 550, width=0, fill='red')

canv.place(x=0,y=0)
ventana.mainloop()









