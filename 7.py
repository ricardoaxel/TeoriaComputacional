#AJEDREZ
import sys
import time
import random
sys.setrecursionlimit(1000)
from tkinter import*

todosarc = open('CaminosT7.txt','w')
ganadoresarc = open('CaminosG7.txt','w+')
ganadores2arc = open('CaminosG27.txt','w+')

#ajedrez

pasos = ["12","14","15","21","23","24","25","26","32","35","36","41","42","45","47","48","51","52","53","54","56","57","58","59","62","63","65","68","69","74","75","78","84","85","86","87","89","95","96","98"]
caminos = {}
caminos2 = {}

arcact = 0 #sirve para ubicarse entre un archivo u otro

n = 3

#n = int(input())

def bfs(tamanio_camino, camino):
	if(tamanio_camino == n):

		if(arcact==0): #añadiendo caminos para la ficha 1
			caminos[camino] = 1

		else: #añadiendo caminos para la ficha 2
			caminos2[camino] = 1
		
		todosarc.write(camino)
		todosarc.write(",")
		return

	for i in range(len(pasos)):
		t = pasos[i]
		if(t[0] == camino[-1]):
			if(tamanio_camino+1 <= n): 
				bfs(tamanio_camino+1, camino+t)

for i in range(3): #Revisando pasos que empiecen con 1
	bfs(1, pasos[i])
	todosarc.write("\n")


arcact = 1 #Con esto cambiamos de ficha
for j in range(3,8): #Revisando pasos que empiecen con 2
	bfs(1, pasos[j])

#Para encontrar los ganadores del
print("Caminos: %d"%len(caminos))

ganadores= []

for x in caminos:
	if x[-1]=="9":
		ganadores.append(x)
		ganadoresarc.write(x)
		ganadoresarc.write(",")


ganadores2= []
for y in caminos2:
	if y[-1]=="8":
		ganadores2.append(y)
		ganadores2arc.write(y)
		ganadores2arc.write(",")
#print (ganadores)

ganaleatorio1 = ganadores[random.randrange(0, len(ganadores))]
ganaleatorio2 = ganadores2[random.randrange(0, len(ganadores2))]


print(ganaleatorio1)
print(ganaleatorio2)


def caminonocruzado(ganaleatorio):
	for p in range(len(ganaleatorio)):
		if (ganaleatorio[p] == ganaleatorio1[p]):
			ganaleatorio = ganadores2[random.randrange(0, len(ganadores2))]
			caminonocruzado(ganaleatorio)
			
		else:
			if(ganaleatorio[p] == "8"):
				return ganaleatorio

ganaleatorio2c = caminonocruzado(ganaleatorio2)

print("\nCamino corregido sin cruces:")



caminoficha1=[1]
for paso in ganaleatorio1:
	if paso[-1] == "1":
		caminoficha1.append(1)
	if paso[-1] == "2":
		caminoficha1.append(2)
	if paso[-1] == "3":
		caminoficha1.append(3)
	if paso[-1] == "4":
		caminoficha1.append(4)
	if paso[-1] == "5":
		caminoficha1.append(5)
	if paso[-1] == "6":
		caminoficha1.append(6)
	if paso[-1] == "7":
		caminoficha1.append(7)
	if paso[-1] == "8":
		caminoficha1.append(8)
	if paso[-1] == "9":
		caminoficha1.append(9)
		caminoficha1.append(9)

caminoficha2=[2]
for paso in ganaleatorio2c:
	if paso[-1] == "1":
		caminoficha2.append(1)
	if paso[-1] == "2":
		caminoficha2.append(2)
	if paso[-1] == "3":
		caminoficha2.append(3)
	if paso[-1] == "4":
		caminoficha2.append(4)
	if paso[-1] == "5":
		caminoficha2.append(5)
	if paso[-1] == "6":
		caminoficha2.append(6)
	if paso[-1] == "7":
		caminoficha2.append(7)
	if paso[-1] == "8":
		caminoficha2.append(8)
		caminoficha2.append(8)
	if paso[-1] == "9":
		caminoficha2.append(9)

caminof1final=[]
caminof2final=[]

for cf1 in caminoficha1[::2]:
	caminof1final.append(cf1)

for cf2 in caminoficha2[::2]:
	caminof2final.append(cf2)
print("Ficha 1:")
print(caminof1final)
print("\nFicha 2:")
print(caminof2final)

#Gráficos

ventana = Tk()
canv = Canvas(ventana,width=600,height=600)
ventana.geometry("600x600")

canv.create_rectangle(0, 0, 200, 200, width=0, fill='red')
canv.create_rectangle(200, 0, 400, 200, width=0, fill='black')
canv.create_rectangle(400, 0, 600, 200, width=0, fill='red')

canv.create_rectangle(0, 200, 200, 400, width=0, fill='black')
canv.create_rectangle(200, 200, 400, 400, width=0, fill='red')
canv.create_rectangle(400, 200, 600, 400, width=0, fill='black')

canv.create_rectangle(0, 400, 200, 600, width=0, fill='red')
canv.create_rectangle(200, 400, 400, 600, width=0, fill='black')
canv.create_rectangle(400, 400, 600, 600, width=0, fill='red')

canv.pack() 

xspeed=5
yspeed=0


tk= Tk()

for x in range(len(caminoficha2)):

	if (caminoficha1[x]==1):
		ball = canv.create_oval(50,50,150,150,fill="#61B8C4")

	if (caminoficha1[x]==2):
		ball = canv.create_oval(250,50,350,150,fill="#61B8C4")

	if (caminoficha1[x]==3):
		ball = canv.create_oval(450,50,550,150,fill="#61B8C4")

	if (caminoficha1[x]==4):
		ball = canv.create_oval(50,250,150,350,fill="#61B8C4")

	if (caminoficha1[x]==5):
		ball = canv.create_oval(250,250,350,350,fill="#61B8C4")

	if (caminoficha1[x]==6):
		ball = canv.create_oval(450,250,550,350,fill="#61B8C4")

	if (caminoficha1[x]==7):
		ball = canv.create_oval(50,450,150,550,fill="#61B8C4")
	
	if (caminoficha1[x]==8):
		ball = canv.create_oval(250,450,350,550,fill="#61B8C4")

	if (caminoficha1[x]==9):
		ball = canv.create_oval(450,450,550,550,fill="#2688E5")
		ball2= canv.create_oval(475,425,525,450,fill="#46DF0C")
#ficha2

	if (caminoficha2[x]==1):
		ball2 = canv.create_oval(50,50,150,150,fill="#E334F5")

	if (caminoficha2[x]==2):
		ball2 = canv.create_oval(250,50,350,150,fill="#E334F5")

	if (caminoficha2[x]==3):
		ball2 = canv.create_oval(450,50,550,150,fill="#E334F5")

	if (caminoficha2[x]==4):
		ball2 = canv.create_oval(50,250,150,350,fill="#E334F5")

	if (caminoficha2[x]==5):
		ball2 = canv.create_oval(250,250,350,350,fill="#E334F5")

	if (caminoficha2[x]==6):
		ball2 = canv.create_oval(450,250,550,350,fill="#E334F5")

	if (caminoficha2[x]==7):
		ball2 = canv.create_oval(50,450,150,550,fill="#E334F5")
	
	if (caminoficha2[x]==8):
		ball2 = canv.create_oval(250,450,350,550,fill="#E600ED")
		ball2 = canv.create_oval(275,425,325,450,fill="#46DF0C")

	if (caminoficha2[x]==9):
		ball2 = canv.create_oval(450,450,550,550,fill="#E334F5")

	tk.update()
	time.sleep(.7)

canv.place(x=0,y=0)
ventana.mainloop()







