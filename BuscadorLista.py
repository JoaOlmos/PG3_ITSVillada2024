def buscador(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
    else:
        return -1

numero = int(input("Introduce el elemento que quieres buscar: "))
resultado = buscador([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], numero)

if resultado != -1:
    print("se encuentra en la posicion: ", resultado)
else:
    print("no se encuentra en la lista")