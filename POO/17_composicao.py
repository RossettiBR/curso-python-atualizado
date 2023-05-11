class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []

    def inserir_endereco(self, rua, numero):
        self.endereco.append(Endereco(rua, numero))

    def listar_endereco(self):
        for endereco in self.endereco:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Rua Calango', 123)
cliente1.listar_endereco()
