# python nao tem modificadores de acesso

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso e privado'

    def metodo_publico(self):
        return 'Metodo publico'

    def metodo_protegido(self):
        return 'Metodo protegido'

    def metodo_private(self):
        return 'Metodo privado'


f = Foo()
print(f.public)
print(f.metodo_publico())
print(f.metodo_protegido())
print(f.metodo_private())