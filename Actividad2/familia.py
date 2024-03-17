class Familia():
    def __init__(self):
        self.padre = str(input("Ingrese el nombre del padre: "))
        self.madre = str(input("Ingrese el nombre de la madre: "))
        self.hijos = []
        for i in range(5):
            self.hijos.append(str(input("Ingrese el nombre del hijo: "))) 

        self.__str__(self.padre, self.madre, self.hijos)

    def __str__(self, padre, madre, hijos: list):
        print(f"El padre es {padre}, la madre es {madre}, los hijos son {hijos}")

familia = Familia()