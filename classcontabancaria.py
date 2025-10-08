# Crie uma classe ContaBancaria com os atributos privados titular e saldo.

# Crie métodos para depositar, sacar e mostrar saldo.

# Garanta que não seja possível sacar mais do que o saldo disponível.

class ContaBancaria:
    def __init__(self,titular,saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self,valor):
        if valor>0:
            self.__saldo += valor
            print('Deposito concluído')
        else:
            print('Valor inválido')

    
    def sacar(self,valor):
        if self.__saldo < valor:
            print('Erro, saldo insuficiente')
        else:
            print(f'Valor de R${valor} reais sacado')
            self.__saldo -= valor
        
    def mostrar_saldo(self):
        print(f'O saldo atual é de R${self.__saldo} reais')

cliente1 = ContaBancaria('Monaliza',1500)
cliente1.mostrar_saldo()
cliente1.sacar(1000)
cliente1.mostrar_saldo()
cliente1.sacar(600)