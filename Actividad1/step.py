def Step (numero):
    cadena_numero = str(numero)
    for i in range(len(cadena_numero) -1):
        if abs(int(cadena_numero[i])-int(cadena_numero[i+1])) !=1:
            return False
    return True



numero = int(input("Introduce un numero: "))
resultado = Step((numero)) 

if resultado == True:
    print("Es un numero step")
else:
    print("No es un numero step")