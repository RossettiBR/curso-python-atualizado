def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Maria')
adiciona_clientes('Carmem', cliente2)
print(cliente2)
