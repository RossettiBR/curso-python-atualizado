def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name} ({class_dict})'
    return class_repr


def adicionar_repr(cls):
    cls.__repr__ = meu_repr
    return cls


def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Você está em casa'

        return resultado
    return interno


@adicionar_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar(self):
        return f'O planeta é {self.nome}'


terra = Planeta('Terra')
caxias = Time('Caxias')
marte = Planeta('Marte')
print(terra)
print(caxias)
print(marte)

print(terra.falar())
print(marte.falar())
