from biblioteca import Pessoa

aluno01 = Pessoa("Vitor", 29, 57 )
print(f"{aluno01.nome} tem {aluno01.idade} anos e pesa {aluno01.peso}kg")


aluno01.comer()
aluno01.dormir()
aluno01.falar()

