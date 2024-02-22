from enum import Enum

class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "estoy comiendo"

class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def comer(self):
        return "estoy comiendo "

    def mostrar_datos(self):
        print(f"Me llamo {self.nombre}, mi raza es {self.raza} y {self.comer()}")

class Aguila(Animal):
    def __init__(self, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo)

    def volar(self):
        return "estoy volando"
    
    def mostrar_datos(self):
        print(f"soy un {self.tipo} y {self.volar()}")

class Tipo(Enum):
    VERTEBRADO = "Vertebrado"
    INVERTEBRADO = "Invertebrado"
    CANINO = "Canino"
    AVE = "Ave"

class Raza(Enum):
    ROTWAILER = "Rotwailer"
    DOGO = "Dogo" 
    BRETON = "Breton"
    PASTOR_ALEMAN = "Pastor Alemán"

perro1 = Perro(4, Tipo.CANINO.value, "Milo", Raza.BRETON.value)
perro1.mostrar_datos()

perro2 = Perro(4, Tipo.CANINO.value, "Carancho", Raza.PASTOR_ALEMAN.value)
perro2.mostrar_datos()

aguila1 = Aguila(2, Tipo.AVE.value)
aguila1.mostrar_datos()
aguila2 = Aguila(2, Tipo.AVE.value)
aguila2.mostrar_datos()