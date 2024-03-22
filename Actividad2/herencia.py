class Persona():
    def __init__ (self):
        self.nombre = str(input("Ingrese el nombre de la persona: "))
        self.edad = int(input("Ingrese la edad de la persona: "))
        self.Mostrar(self.nombre)

    def Mostrar(self, nombre):
        print(f"Hola {self.nombre}")

class Empleado(Persona):

    def __init__ (self):
        super().__init__()
        self.sueldo = int(input("Ingrese el sueldo del empleado: "))
        self.Impuestos(self.sueldo)

    def Impuestos(self, sueldo):
        if self.sueldo > 3000:
            print(f"Su sueldo es de {self.sueldo} y tiene impuestos")
        else:
            print(f"Su sueldo es de {self.sueldo} y no tiene impuestos")

persona = Persona()
empleado = Empleado()