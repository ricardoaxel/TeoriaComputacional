#PROTOCOLO PRUEBAS CON AUTOMATA DE PARIDAD

import random
import threading
from tkinter import*

cadprueba = []

def gen(identificador):
	numbinalt = []
	fop = open("Datos4/Protocolo paridad" + str(identificador) + ".txt", "w")
	for i in range(1000):
		rand = random.randrange(10000)
		cadprueba = str(bin(rand)[2:])
		paridad(cadprueba, fop)

def paridad(palabra, archivo):
    c = 0
    for x in palabra:
        #estado 0
    	if (c == 0 and x == "0"):
    		c = 1
    		continue
    	if (c == 0 and x == "1"):
    		c = 3
    		continue

        #estado 1
    	if (c == 1 and x == "0"):
    		c = 0
    		continue
    	if (c == 1 and x == "1"):
    		c = 2
    		continue

        #estado 2
    	if (c == 2 and x == "1"):
    		c = 1
    		continue
    	if (c == 2 and x == "0"):
    		c = 3
    		continue

        #estado 3
    	if (c == 3 and x == "0"):
    		c = 2
    		continue
    	if (c == 3 and x == "1"):
    		c = 0
    		continue

    if (c == 0):
    	archivo.write("Par  : "+palabra+" \n\n")

    else:
        archivo.write("Impar: "+palabra+" \n\n")


n = random.randrange(100) #rango de pruebas aleatorio

print ("Número de pruebas a realizar:",n)

for i in range(n):
    if random.randint(0, 1) == 1:
        print ("\nPrueba "+str(i+1)+": Protocolo "+str(i)+" corriendo.")
        t = threading.Thread(target = gen, args = (i,))
        t.start()
        t.join()
    else:
        print ("\nPrueba "+str(i+1)+": El Protocolo no inició.")



##############

#Gráficos

ventana = Tk()
canv = Canvas(ventana,width=800,height=300)
ventana.geometry("800x300")

ventana.title('Automata Paridad')

p= Label(ventana,text="Cadena a verificar. \n Cadena:").place(x=10,y=10)

#q0
p0= Label(ventana,text="Ready").place(x=50,y=105)
	
canv.create_oval(20,70,110,160, fill="blue")


canv.create_oval(35,85,95,145)
n1= Label(ventana,text="data in").place(x=185,y=35)

canv.create_oval(40,155,50,165, fill="black")
canv.create_oval(90,145,100,155, fill="black")

n2= Label(ventana,text="Start").place(x=25,y=185)

n2= Label(ventana,text="ack").place(x=185,y=175)

#q1
p1= Label(ventana,text="Sending").place(x=290,y=105)
canv.create_oval(270,70,360,160, fill="blue")

canv.create_oval(280,75,290,85, fill="black")


canv.create_oval(312,65,322,75, fill="black")

n1= Label(ventana,text="timeout").place(x=300,y=35)


#lineas

canv.create_line(35, 185, 45, 160, width=2, fill='black')

xy1 = 95, 60, 286, 105
canv.create_arc(xy1, start=0, extent=180, style="arc")

xy1 = 95, 125, 286, 170
canv.create_arc(xy1, start=0, extent=-180, style="arc")

xy2 = 316, 40, 356, 120
canv.create_arc(xy2, start=-25, extent=200, style="arc")

canv.place(x=0,y=0)
ventana.mainloop()