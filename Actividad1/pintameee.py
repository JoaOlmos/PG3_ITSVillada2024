while True:
    respuesta = int(input("Desea pintar un cuadrado o un triangulo? (1 ó 2): "))

    if respuesta == 1:
        ancho = int(input("Ingrese el ancho de la matriz: "))
        alto = int(input("Ingrese el alto de la matriz: "))
        caracter = str(input("Ingrese el caracter a usar: "))

        for i in range(alto):
            for j in range(ancho):
                print(caracter, end="")
            print()
        break

    elif respuesta == 2:
        alto = int(input("Ingrese el alto de la matriz: "))
        caracter = str(input("Ingrese el caracter a usar: "))
        
        for i in range(alto):
            for j in range(i+1):
                print(caracter, end="")
            print()
        break
    else:
        print("Opcion no valida")
        continue


