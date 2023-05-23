from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'Valor'
    naipe: str = 'Naipe'


if __name__ == '__main__':
    carta1 = Carta('espada', 'As')
    print(carta1)