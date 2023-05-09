class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metedo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anonimo', idade)


p1 = Pessoa('Joao', 23)
Pessoa.metedo_de_classe()
p3 = Pessoa.criar_com_50_anos('helena')
p4 = Pessoa.criar_sem_nome(43)
print(p1.nome, p1.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
