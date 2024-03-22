class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
        self.Mostrar(self.nombre)

    def Mostrar(self, nombre):
        print(f"Hola {self.nombre}")
    
persona1 = Persona("joa")
persona2 = Persona("emi")