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
    def parar_falar(self):
        if self.falando:
            self.falando = False
            print("Parou de falar")
        else:
            print("Já parou de falar")

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
    def parar_comer(self):
        if self.comendo:
            self.comendo = False
            print("Parou de comer")
        else:
            print("Já parou de comer")

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
    def acordar(self):
        if self.dormindo:
            self.dormindo = False
            print("Acordou")
        else:
            print("Já está acordaro")


class ContaBanco():
    def __init__(self, num, nome, tipo):
        self.num = num
        self.nome = nome
        self.tipo = tipo

        self.status = False
        self.saldo = 0

    def ativarConta(self):
        if self.status == False:
            self.status = True
        else:
            print("A conta já está ativa")

    def depositar(self, deposito):
        if self.status == True:
            self.saldo = deposito

    def verificarSaldo(self):
        print(self.saldo)

    def sacar (self):

        #Aqui precisa reformular para saque negativado.

        if self.status == True:
            if self.saldo == 0:
                print("Você não tem saldo na conta")
            elif self.saldo < 0:
                print("Você está negtivado")
            else:
                print("Quanto deseja sacar")











