class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
    
    def apresentacao(self):
        print(f'Olá {self.nome} seja bem-vindo(a) ao nosso programa!')

dados_das_pessoas = [
    {'Nome':'Eduarda','Idade':24},
    {'Nome':'Fábio','Idade':45},
    {'Nome':'Roberto','Idade':36}
]
listar_pessoas = []
for dados in dados_das_pessoas:
    nova_pessoa = Pessoa(dados['Nome'],dados['Idade'])
    listar_pessoas.append(nova_pessoa)

print('Lista de pessoas cadastradas')
for pessoa in listar_pessoas:
    pessoa.apresentacao()
    


