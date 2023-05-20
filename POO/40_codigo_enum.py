import enum


class Direcao(enum.Enum):
    DIREITA = enum.auto()
    ESQUERDA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


def mover(direcao: Direcao):
    if not isinstance(direcao, Direcao):
        raise ValueError('Direção não encontrada')
    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcao.ESQUERDA)
mover(Direcao.DIREITA)
mover(Direcao.ACIMA)
mover(Direcao.ABAIXO)
