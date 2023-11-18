def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        # Verificar si el elemento está en la mitad
        if lista[medio] == elemento:
            return medio
        # Si el elemento está en la mitad izquierda
        elif lista[medio] > elemento:
            fin = medio - 1
        # Si el elemento está en la mitad derecha
        else:
            inicio = medio + 1

    return -1  # Retorna -1 si el elemento no está en la lista

# Ejemplo de uso
lista_ordenada = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
elemento_a_buscar = 12

resultado = busqueda_binaria(lista_ordenada, elemento_a_buscar)

if resultado != -1:
    print(f"El elemento {elemento_a_buscar} está en la posición {resultado} de la lista.")
else:
    print(f"El elemento {elemento_a_buscar} no está en la lista.")
