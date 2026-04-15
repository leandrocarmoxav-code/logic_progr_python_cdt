'''
class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def buzinar(self):
        print(f'O {self.marca} da cor {self.cor} fez Bip Bip!')

meu_carro = Carro('Toyota', ' cinza')

carro_do_cliente = Carro('Honda', 'preto')

meu_carro.buzinar()

carro_do_cliente.buzinar()


'''

class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.bateria = 100


    def ligar(self):
        self.ligado = True
        print(f'{self.modelo} esta ligado.')


    def carregar(self):
        self.bateria = 100
        print(f'{self.modelo} esta carregado.')


meu_celular = Celular('Xiaomi', 'Poco x7 Pro')
meu_celular.ligar()
meu_celular.carregar()
meu_celular.bateria = 5
print(f'{meu_celular.modelo} está com {meu_celular.bateria}% de bateria.')