class Pessoa():
    def __init__(self, nome, idade, peso ):
        self.nome=nome
        self.idade=idade
        self.peso=peso

        self.comendo=False
        self.falando=False
        self.dormindo=False

    def falar(self):
        if self.comendo:
            print("Não pode falar, já está comendo.")
        elif self.dormindo:
            print("Não pode falar, está dormindo")
        elif self.falando:
            print("Não pode falar, já está falando")
        else:
            self.falando = True
            print("Começou a falar")

    def comer(self):
        if self.comendo:
            print("Não pode comer, já está comendo.")
        elif self.falando:
            print("Não pode comer, está falando")
        elif self.dormindo:
            print("Não pode comer, está dormindo")
        else:
            self.comendo = True
            print("Começou  a comer")

    def dormir(self):
        if self.comendo:
            print("Não pode dormir, já está comendo.")
        elif self.falando:
            print("Não pode dormir, está falando")
        elif self.dormindo :
            print("Não pode dormir, já está dormindo")
        else:
            self.dormindo = True
            print(f"{self.nome} começou a dormir")