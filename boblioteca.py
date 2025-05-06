class Pessoa():
    def __init__(self, nome, idade, peso, comendo, falando, dormindo ):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.falando=False
        self.dormindo=False

    def falar(self):
        print(f"{self.nome} começou a falar")
    def comer(self, comida):
        if self.comendo == True:
            print("Não pode, já está comendo.")
        print(f"{self.nome} começou a comer{comida}")
    def dormir(self):
        print(f"{self.nome} começou a dormir")