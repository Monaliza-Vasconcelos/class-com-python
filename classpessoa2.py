# Na classe Pessoa, adicione um método apresentar() que imprime:
# Olá, meu nome é <nome> e tenho <idade> anos.

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade}')

pessoa1 = Pessoa('Monaliza',27)
pessoa1.apresentar()