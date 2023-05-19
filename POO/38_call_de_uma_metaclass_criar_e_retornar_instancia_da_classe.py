def meu_repr(self):
    return f'{type(self).__name}{(self.__dict__)}'


class Meta(type):
    def __new__(mcs, name, base, dct):
        cls = super().__new__(mcs, name, base, dct)
        cls.attr = 1234
        cls.__repr__= meu_repr

        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')

        return cls

    def __call__(self, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')

        return instancia


class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Meu New')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('Meu init')
        self.nome = nome

    def falar(self):
        print('Falando...')


p1 = Pessoa('Wander')
p1.falar()
