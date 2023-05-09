import json
CAMINHO_ARQUIVO = 'aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('joão', 33)
p2 = Pessoa('maria', 24)
p3 = Pessoa('joana', 45)
bd = [vars(p1), p2.__dict__, vars(p3)]


def fazendo_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
