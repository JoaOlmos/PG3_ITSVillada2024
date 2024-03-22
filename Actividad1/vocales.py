def vocales (frase):
    contador = 0
    las_vocales = ("a", "e", "i", "o", "u")
    frase = frase.replace(' ','')
    frase = frase.lower()

    for i in frase:
        if i in las_vocales:
            contador += 1

    return contador

frase = str(input("Introduce una frase: "))
resultado = vocales(frase)

print(f"La frase {frase} tiene {resultado} vocales")