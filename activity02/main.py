class Veiculo:
    def __init__(self):
        self.cor = None
        self.modelo = None

    def set_cor(self, cor):
        self.cor = cor
        return self

    def set_modelo(self, modelo):
        self.modelo = modelo
        return self

    def __str__(self):
        return f"Veículo - Cor: {self.cor}, Modelo: {self.modelo}"

class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = "Carro"

    def __str__(self):
        return f"{self.tipo} - Cor: {self.cor}, Modelo: {self.modelo}"

class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = "Bicicleta"

    def __str__(self):
        return f"{self.tipo} - Cor: {self.cor}, Modelo: {self.modelo}"

carro = Carro().set_cor("Vermelho").set_modelo("Porshe")
bicicleta = Bicicleta().set_cor("Azul").set_modelo("Caloi 10")

print(carro)
print(bicicleta)
