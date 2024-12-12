import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)
if __name__ == "__main__":
    # Crear un círculo con radio 5
    circulo = Circulo(5)
    print(f"Área del círculo: {circulo.area()}")
    print(f"Perímetro del círculo: {circulo.perimetro()}")

    # Crear un rectángulo con largo 4 y ancho 6
    rectangulo = Rectangulo(4, 6)
    print(f"Área del rectángulo: {rectangulo.area()}")
    print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")
