lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.append(10)
print(lista)
lista.append(11)
print(lista)

print()

lista.pop()
print(lista)
print()

from collections import deque

fila_correta: deque[int] = deque()
fila_correta.append(3)
fila_correta.append(4)
fila_correta.append(5)
fila_correta.appendleft(2)
fila_correta.appendleft(1)
fila_correta.appendleft(0)
print(fila_correta)
