try:
    with open("archivo.txt", "w") as archivo:
        enteros = [1, 12, 4, 5, 56, 6]
        for string in enteros:
            archivo.write(string + "\n")

except TypeError as e:
    print("Error:", e)
    print("Se intentó escribir un tipo de dato incorrecto en el archivo.")