from class_numero_aleatorio import NumeroAleatorio

num = NumeroAleatorio()
long = int(input("ingrese la longitud de la lista: "))
listaAleatorios = num.generarListaAleatoria(long)
coincidencias = num.contarRepetidos()
print("\nNumeros aleatorios:", listaAleatorios, "\n")


for key, value in coincidencias.items():
    if key <=10:
        print(f"{key}: hubo {value}")