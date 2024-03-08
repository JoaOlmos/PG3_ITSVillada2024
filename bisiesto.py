def bisiesto(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return True
    else:
        return False

year = int(input("Ingrese el año que quiera comprobar: "))
resultado = bisiesto(year)

if resultado == True:
    print("El año es bisiesto")
else :
    print("el año no es bisiesto")
