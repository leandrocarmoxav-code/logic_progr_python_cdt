'''



'''

class celular:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo
        self.bateria = 100

    def fazer_chamada(self, custo_bateria):
        print(f"\n--- Chamada no {self.modelo} ---")
        try:
            self.bateria -= custo_bateria
        except TypeError:
            print("ERRO: O custo da bateria deve ser um numero!")
        else:
            print(f"Sucesso! Bateria Atual: {self.bateria}%")
        finally:
            print("Sistema finalizado.")

meu_celular = celular("Samsung", "S24")
meu_celular.fazer_chamada("muito") 