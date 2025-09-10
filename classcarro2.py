# Na classe Carro, adicione um método ligar() que imprime "O carro está ligado" e outro desligar() que imprime "O carro está desligado".

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__ligado = False #Atributo privado

    def info_carro(self):
        print(f'Marca: {self.marca} Modelo: {self.modelo} Ano: {self.ano}')
    
    def ligar(self):
        if not self.__ligado:
            print('O carro está desligado, ligando...')
            self.__ligado = True
            print('O carro foi ligado')
        else:
            print('O carro já está ligado')
    
    def desligar(self):
        if self.__ligado:
            print('O carro estava ligado, desligando')
            self.__ligado = False
            print('O carro foi desligado')
        else:
            print('O carro já está desligado...')
            
carro1 = Carro('Toyota','Corolla',2022)
carro1.info_carro()
carro1.ligar()
carro1.desligar()