# import sys
from sys import exit, platform


def hello_world(msg):
    return msg


def soma(n1, n2):
    soma = n1 + n2
    return soma


ola = hello_world('Olá mundo')
print(ola)
soma = soma(1, 3)
print(soma)


# platform = 'A minha '
print(platform)

