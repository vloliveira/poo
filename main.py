from boblioteca import Pessoa

aluno01 = Pessoa("Vitor", 29, 57 )
aluno02 = Pessoa("Guilherme", 21, 82 )
print(f"{aluno01.nome} tem {aluno01.idade} anos e pesa {aluno01.peso}kg")
aluno01.nome = "Vitor Lopes de Oliveira"
print(f"{aluno02.nome} tem {aluno02.idade} anos e pesa {aluno02.peso}kg")



aluno01.falar()
aluno01.comer("Pipoca")
aluno01.dormir()