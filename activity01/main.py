import math

class Forma:
    def area(self):
        pass
    def perimetro(self):
        pass
class Circulo(Forma):
    def __init__(self,raio):
        self.raio = raio
    def area(self):
        return math.pi * self.raio ** 2
    def perimetro(self):
        return 2 * math.pi * self.raio
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
    def perimetro(self):
        return 4 * self.lado
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
    def perimetro(self):
        return 2 * (self.largura + self.altura)


circulo = Circulo(5)
print(f"Circulo - área: {circulo.area():.2f} cm², perímetro: {circulo.perimetro():.2f} cm")

retangulo = Retangulo(4, 6)
print(f"Retângulo - área: {retangulo.area()} cm², perímetro: {retangulo.perimetro()} cm")

quadrado = Quadrado(4)
print(f"Quadrado - área: {quadrado.area()} cm², perímetro: {quadrado.perimetro()} cm")

