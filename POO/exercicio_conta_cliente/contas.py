from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhe(f'(DEPÓSITO {valor})')
        return self.saldo

    def detalhe(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('---')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhe(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')
        self.detalhe(f'(SAQUE NEGADO {valor})')


class ContaCorrente(Conta):
    def __init__(
            self, agencia: int, conta: int,
            saldo: float = 0, limite: float = 0
    ):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhe(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhe(f'(SAQUE NEGADO {valor})')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
                f'{self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    # cp1 = ContaPoupanca(111, 22, 0)
    # cp1.sacar(1)
    # cp1.depositar(1)
    # cp1.sacar(1)
    print('#' * 10)
    cc1 = ContaCorrente(111, 22, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)