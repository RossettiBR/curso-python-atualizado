# class MinhaString(str):
#     def upper(self):
#         return super().upper()


# string = MinhaString('Wander')
# print(string.upper())

class A:
    atributo_a = 'valor a'

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def metodo(self):
        print('C')


c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
