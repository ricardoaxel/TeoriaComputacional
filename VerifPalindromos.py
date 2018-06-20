#VERIFICADOR DE PALINDROMOS
ar = open("Datos10.txt", "w")

print("Verificador de palindromos, Ingrese la cadena a evaluar:")
ar.write("\n"+"Verificador de palindromos, Cadena a evaluar:")

ingr = input() #cadena a evaluar
cad1= (ingr.replace(" ", "")).lower() #estandarizando las cadenas
print(cad1)
ar.write("\n"+cad1)
cad= list(cad1)

tamcad = len(cad)
verificador = 0
micha = int(tamcad/2)

if(tamcad%2 == 1): #si la cadena es impar tomamos la letra del centro como mitad
	micha = int(tamcad/2)

if(tamcad%2 == 0): #si no es par creamos un centro 'x'
	cad.insert(micha,"x")
	
print(cad)
ar.write("\n"+str(cad))

cadenaformada = cad[micha]
print("Comenzando en: "+cad[micha]+"\n")
ar.write("\n"+"Comenzando en: "+cad[micha]+"\n")

for i in range(1,micha+1):
	if cad[micha-i] == cad[micha+i]:
		verificador = verificador+1
		cadenaformada = cad[micha-i]+cadenaformada+cad[micha+i] 
		print(cadenaformada+ "   /")
		ar.write("\n"+cadenaformada+ "   /")
	else:
		print(cadenaformada+ "   X")
		ar.write("\n"+cadenaformada+ "   X")
		break

if(verificador==micha):
	print("\nEs un palíndromo")
	ar.write("\n"+"\nEs un palíndromo")

else:
	print("\nNO es un palíndromo")
	ar.write("\n"+"\nNO es un palíndromo")


