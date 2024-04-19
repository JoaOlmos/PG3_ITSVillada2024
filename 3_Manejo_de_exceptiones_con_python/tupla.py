meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

index = int(input("Ingresa el index de un mes: "))
try:
    if index == meses.index():
        print(f"El mes es {meses[index]}")
except IndexError:
    print("El index no existe")
