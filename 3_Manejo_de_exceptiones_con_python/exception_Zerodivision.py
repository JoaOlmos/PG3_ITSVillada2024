try :
    num = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))
    print("Resultado:",num/num2)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
