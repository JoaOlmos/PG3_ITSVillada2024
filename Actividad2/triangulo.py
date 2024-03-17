class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.mayor(self.lado1, self.lado2, self.lado3)
        self.equilatero(self.lado1, self.lado2, self.lado3)

    def mayor(self, lado1, lado2, lado3):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(f"El lado mayor es {self.lado1}")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print(f"El lado mayor es {self.lado2}")
        else:
            print(f"El lado mayor es {self.lado3}")

    def equilatero(self, lado1, lado2, lado3):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print(f"El triangulo es equilatero")
        else:
            print(f"El triangulo no es equilatero")

triangulo1 = Triangulo(1, 2, 3)