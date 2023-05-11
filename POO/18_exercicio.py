class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = []
        self.fabricante = []

    def inserir_motor(self, nome):
        self.motor.append(Motor(nome))

    def inserir_fabricante(self, nome):
        self.fabricante.append(Fabricante(nome))

    def listar_motor_fabricante(self):
        for motor in self.motor:
            for fabricante in self.fabricante:
                print(f'{self.nome} tem o motor {motor.nome} do fabricante {fabricante.nome}')


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


carro1 = Carro('Gol')
carro1.inserir_motor('Ap 1.6mi')
carro1.inserir_fabricante('VW')
carro1.listar_motor_fabricante()
