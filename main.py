from biblioteca import Pessoa, ContaBanco

"""aluno01 = Pessoa("Vitor", 29, 57 )
print(f"{aluno01.nome} tem {aluno01.idade} anos e pesa {aluno01.peso}kg")

aluno01.falar()
aluno01.parar_falar()
aluno01.comer()
aluno01.parar_comer()
aluno01.dormir()
aluno01.acordar()
aluno01.acordar()"""

cliente = ContaBanco("12354","Vitor","Corrente")

cliente.ativarConta()
cliente.verificarSaldo()
cliente.depositar(200)
cliente.verificarSaldo()
cliente.sacar(200)
cliente.verificarSaldo()