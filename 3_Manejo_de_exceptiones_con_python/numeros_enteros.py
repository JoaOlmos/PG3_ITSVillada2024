try :
    while True:
        num = int(input("Ingrese un numero entero: "))
        num2 = int(input("Ingrese otro numero entero: "))
        print(num+num2)
        salir = str(input("Desea continuar? (s/n): "))
        salir = salir.lower()
        if salir == "s":
            continue
        else:
            break
except ValueError:
    print("No es un numero entero")
