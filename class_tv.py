class Televisao():
  def __init__(self, n_canais):
      self.n_canais = n_canais

  
  def aumentar_canal(self,valor):
      self.n_canais += valor

  
  def diminuir_canal(self,valor):
      self.n_canais -= valor


#programa principal

print('[1] Aumentar canal')
print('[2] Diminuir canal')
while True:
    try:
        resposta = input('Escolha uma opção: ')
        if resposta == '1':
            aumento = int(input('Deseja aumentar quantos canais? '))
            tv = Televisao(20)
            tv.aumentar_canal(aumento)
            print(f'Canais atuais: {tv.n_canais}')
            break
        elif resposta == '2':
            diminuir = int(input('Deseja diminuir quantos canais? '))
            tv = Televisao(20)
            tv.diminuir_canal(diminuir)
            print(f'Canais atuais: {tv.n_canais}')
            break
        else:
            print('\033[0;33mDigite uma opção válida\033[m')
    except ValueError:
        print('\033[0;33mDigite um valor válido\033[m')
