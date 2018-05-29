#VERIFICADOR DE PALINDROMOS
print("Verificador de palindromos")

cad = input() #cadena a evaluar

tamcad = len(cad)
micha = int(tamcad/2)

verificador = 0
aux = 0

for i in range(0,micha):
	print("Comparando "+cad[i]+" con "+cad[-i-1])
	if cad[i] == cad[-i-1]:
		verificador = verificador+1
		print("Letras iguales")
	else:
		print("letras distintas")
		break


if(verificador==micha):
	print("\nEs un palíndromo")

else:
	print("\nNo es un palíndromo")






