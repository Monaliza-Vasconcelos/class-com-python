class Funcionario:
    def __init__(self,nome,cpf,salario):
        self.nome = nome
        self._cpf = cpf
        self._salario = salario


    def mostra_bonus(self):
        return self._salario * 0.10
    

    def __str__(self):
        return f'Nome: {self.nome} - CPF: {self._cpf} - Salário: R${self._salario:.2f}'
    
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario,senha,qnt_subordinados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qnt_subordinados = qnt_subordinados


    def mostra_bonus(self):
        return self._salario * 0.10 + self._qnt_subordinados * 0.10
    

class Secretaria(Funcionario):
    def __init__(self, nome, cpf, salario,senha, qnt_gerentes):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self._qnt_gerentes  = qnt_gerentes
    

    def mostra_bonus(self):
        return self._salario * 0.10 + self._qnt_gerentes * 0.10

class Bonus_total:
    def __init__(self,total_bonificacao=0):
        self._total_bonificaca = total_bonificacao

    def registra(self,funcionario):
        self._total_bonificaca += funcionario.mostra_bonus()

    @property
    def total_bonificacao(self):
        return self._total_bonificaca
    



g1 = Gerente('Paulo',333,5000,123,10)
s1 = Secretaria('Ana',456,2000,321,5)

gestao = Bonus_total()
gestao.registra(g1)
gestao.registra(s1)

print('-'*40)
print(g1)
print(s1)
print(f'Valor total em bonificações pagas aos funcionários R${gestao.total_bonificacao:.2f}')
print('-'*40)
    


