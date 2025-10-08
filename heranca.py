class Funcionario:
    def __init__(self,nome,cpf,salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario,senha,n_subordinados):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.n_subordinados = n_subordinados
    
    def validacao(self, senha):
        if self.senha == senha:
            return True
        else:
            print('Acesso negado')
            return False
    
g1 = Gerente('Paulo',33333,4000,12345678,2)
print(g1.senha)