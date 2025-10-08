# Crie uma classe chamada Carro com atributos marca, modelo e ano.
# Adicione um método que mostre as informações do carro.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def info_carro(self):
        print(f'Marca: {self.marca} Modelo: {self.modelo} Ano: {self.ano}')

carro1 = Carro('Toyota','Corolla',2022)
carro1.info_carro()