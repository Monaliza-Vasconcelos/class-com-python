# Crie uma classe chamada Pessoa com os atributos nome e idade.
# Depois, crie um objeto dessa classe e mostre seus dados.
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa('Monaliza',27)
print(f'{pessoa1.nome} {pessoa1.idade}')

    