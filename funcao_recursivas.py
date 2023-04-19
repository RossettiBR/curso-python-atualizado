def recursiva(inicio=0, fim=10):
    # Caso base
    if inicio >= fim:
        return fim

    print(inicio, fim)

    # Caso recursivo
    # contar até chegar no final

    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())
