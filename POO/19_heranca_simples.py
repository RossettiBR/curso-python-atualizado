class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente('Wanderson', 'Rossetti')
c1.falar_nome_classe()
a1 = Aluno('Gamora', 'Rossetti')
a1.falar_nome_classe()
