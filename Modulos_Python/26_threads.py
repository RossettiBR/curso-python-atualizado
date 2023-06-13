from time import sleep
from threading import Thread


'''class MeuTempo(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuTempo('Thread 1', 5)
t1.start()

for i in range(20):
    print(i)
    sleep(.5)'''


'''def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo', 5))
t1.start()
t1.join()

print('Fim!!!')
'''


class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade):
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            return

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} de ingressos(s)'
              f'Ainda temos {self.estoque} em estoque')


if __name__ == '__main__':
    ingresso = Ingresso(10)
    for i in range(1, 20):
        ingresso.comprar(i)
