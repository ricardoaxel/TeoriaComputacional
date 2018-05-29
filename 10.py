#VERIFICADOR DE PALINDROMOS
print("Verificador de palindromos, Ingrese la cadena a evaluar:")

ingr = input() #cadena a evaluar
cad= list(ingr)

tamcad = len(cad)
verificador = 0
micha = int(tamcad/2)

if(tamcad%2 == 1): #si la cadena es impar tomamos la letra del centro como mitad
	micha = int(tamcad/2)

if(tamcad%2 == 0): #si no es par creamos un centro 'x'
	cad.insert(micha,"x")
	
print(cad)

print("Comenzando en: "+cad[micha]+"\n")
for i in range(1,micha+1):
	print("Comparando "+cad[micha-i]+" con "+cad[micha+i])
	if cad[micha-i] == cad[micha+i]:
		verificador = verificador+1
		print("Letras iguales")
	else:
		print("Letras distintas")
		break

if(verificador==micha):
	print("\nEs un palíndromo")

else:
	print("\nNO es un palíndromo")


