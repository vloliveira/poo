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

#------------------------------------------------------------------

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

#------------------------------------------------------------------

class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"{self.nome} {self.cor} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"O {self.nome} foi miando...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f"O {self.nome} foi mugindo...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"O {self.nome} foi latindo...")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def grunir(self):
        print(f"O {self.nome} foi grunindo...")

#------------------------------------------------------------------

class Ingresso():
    def __init__(self, valor):
        self.valor = valor
    def imprimeValor (self):
        print(f"O valor do ingresso pista é: {self.valor}")

class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor *= 1.5
    def adicional(self):
        print(f"O valor do ingresso VIP é de {self.valor}")

#------------------------------------------------------------------

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()
        self.base = 0
        self.altura = 0

    def calcularArea(self, base, altura):
        self.area = base * altura
        print(self.area)

    def calcularPerimetro(self, base, altura):
        self.perimetro = 2*(base+altura)
        print(self.perimetro)

class Triangulo(Forma):
    def __init__(self, area, perimetro):
        super().__init__(area, perimetro)

#------------------------------------------------------------------

class Atleta():
    def __init__(self):
        self.aposentado = False
        self.peso = 0

        self.aquecendo = False
        self.correndo = False
        self.nadando = False
        self.pedalando = False

    def aposentar (self):
        self.aposentado = True
        print("Se aposentou!")

    def aquecer (self):
        if self.aposentado:
            print("Não pode aquecer, está aposentado!")
        else:
            self.aquecendo = True
            print("Está se aquecendo!")

class Corredor(Atleta):
    def __init__(self):
        super().__init__()
    def correr(self):
        if self.aposentado == False:
            if self.aquecendo:
                print("Pode correr, já está aquecido!")
                self.correndo = True
            elif self.correndo:
                print("Já está correndo!")
            elif self.nadando:
                print("Não pode correr pois é nadador.")
            elif self.pedalando:
                print("Não pode correr pois é ciclista.")
            else:
                print("Precisa aquecer antes de correr.")
        else:
            print("Não pode correr, está aposentado!")

class Nadador(Atleta):
    def __init__(self):
        super().__init__()
    def nadar(self):
        if self.aposentado == False:
            if self.aquecendo:
                print("Pode nadar, já está aquecido!")
                self.nadando = True
            elif self.nadando:
                print("Já está nadando!")
            elif self.correndo:
                print("Não pode nadar pois é corredor.")
            elif self.pedalando:
                print("Não pode nadar pois é ciclista.")
            else:
                print("Precisa aquecer antes de nadar.")
        else:
            print("Não pode nadar, está aposentado!")

class Ciclista(Atleta):
    def __init__(self):
        super().__init__()
    def pedalar(self):
        if self.aposentado == False:
            if self.aquecendo:
                print("Pode pedalar, já está aquecido!")
                self.pedalando = True
            elif self.pedalando:
                print("Já está pedalando!")
            elif self.correndo:
                print("Não pode correr pois é ciclista.")
            elif self.nadando:
                print("Não pode nadar pois é ciclista.")
            else:
                print("Precisa aquecer antes de pedalar.")
        else:
            print("Não pode nadar, está aposentado!")

"""class TriAtleta(Atleta, Corredor, Nadador, Ciclista):
    def __init__(self):
        super().__init__()"""