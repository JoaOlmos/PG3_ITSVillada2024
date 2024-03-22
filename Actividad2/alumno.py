class Alumno():
    def __init__ (self):
        self.nombre = str(input("Ingrese el nombre del alumno: "))
        self.nota = int(input("Ingrese la nota del alumno: "))
        self.Mostrar(self.nombre, self.nota)
    
    def Mostrar(self, nombre, nota):
        if self.nota >= 7:
            print(f"Hola {self.nombre}, usted esta aprobado tiene una nota regular")
        else:
            print(f"Hola {self.nombre}, usted esta desaprobado no ha cumplido con la nota regular")

alumno1 = Alumno()
alumno2 = Alumno()