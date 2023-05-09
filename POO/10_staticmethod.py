class Classe:
    @staticmethod
    def funcao_que_esta_dentro_da_classe(*args, **kwargs):
        print('oi', args, kwargs)


def funcao(*args, **kwargs):
    print('oi', args, kwargs)


c1 = Classe()
c1.funcao_que_esta_dentro_da_classe(1, 2, 3)
funcao(1, 2, 3)
