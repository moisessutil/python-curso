# class MinhaString(str):
#     def upper(self):
#         print('Chamou o Upper')
#         return super().upper()

# string = MinhaString('Carlos')
# print(string.upper())

class A:
    atributo_a = ('Valor a')

    def metodo(self):
        print('A')

class B(A):
    atributo_b = ('Valor b')

    def metodo(self):
        print('B')

class C(B):
    atributo_c = ('Valor c')

    def metodo(self):
        super().metodo()
        super(B, self).metodo()
        print('C')

c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)

c.metodo()