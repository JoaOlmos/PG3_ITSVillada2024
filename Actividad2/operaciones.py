class Operacion():
    def __init__(self):
        self.entero = int(input("Introduce un numero entero: "))
        self.entero2 = int(input("Introduce otro numero entero: "))
        self.suma(self.entero, self.entero2)
        self.resta(self.entero, self.entero2)
        self.multiplicacion(self.entero, self.entero2)
        self.division(self.entero, self.entero2)

    def suma (self, entero, entero2):
        print(f"La suma de {self.entero} + {self.entero2} = {self.entero + self.entero2}")
    
    def resta (self, entero, entero2):
        print(f"La resta de {self.entero} - {self.entero2} = {self.entero - self.entero2}")
    
    def multiplicacion (self, entero, entero2):
        print(f"La multiplicacion de {self.entero} * {self.entero2} = {self.entero * self.entero2}")
    
    def division (self, entero, entero2):
        print(f"La division de {self.entero} * {self.entero2} = {self.entero / self.entero2}")

Operacion()