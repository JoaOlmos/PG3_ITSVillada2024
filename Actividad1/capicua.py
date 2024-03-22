def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

palabra = str(input('Escribe una palabra para saber si es un palindromo: '))
resultado = palindromo(palabra)

if resultado == True:
    print('Es un palindromo')
else:
    print('No es un palindromo')