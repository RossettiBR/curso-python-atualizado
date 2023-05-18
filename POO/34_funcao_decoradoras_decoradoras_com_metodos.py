def adicionar_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__= meu_repr
    return cls


@adicionar_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


marte = Planeta('Marte')
internacional = Time('Internacional')

print(marte)
print(internacional)
