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

import random

print("1)Modo manual. 2)Modo automático")
opc = input()

if (opc=="1"):
	cad = input() #cadena a evaluar

else:
	rand = random.randrange(10000)
	cad = str(bin(rand)[2:])
cadc = cad[::-1] #cadena invertida para meterla a la pila

print (cadc)

p = Pila()

e = "a" #a son 0's b son 1's
aux1 = 0 #estado de validacion de la cadena (0 invalido 1 valido)

for i in cadc:

	if(cadc[0]=="1"):
		p.push("X")
		print(p.arreglo)
		aux1= aux1+1
		continue

	if(i=="0" and e == "a"):
		p.push(i)
		print(p.arreglo)
		continue

	if(i=="0" and e == "b"):
		continue

	if(i=="1" and e=="a"):
		e="b"
		p.pop()
		print(p.arreglo)
		aux1= aux1+1
		continue

	if(i=="1" and len(p.arreglo)<aux1):
		p.push("X")
		print(p.arreglo)
		aux1= aux1+1
		continue

	if(i=="1" and e=="b"):
		p.pop()
		print(p.arreglo)
		continue




print("\n")
print(p.arreglo)



