class Multiplicar:
    def __init__(self, multiplicador):
        self.multiplicador = multiplicador

    def __call__(self, func):
        def interno(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicador
        return interno


@Multiplicar(10)
def soma(x, y):
    return x + y


soma1 = soma(4, 6)
print(soma1)
