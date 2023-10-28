class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Carlos', 'Alberto')
# p1.nome = 'Carlos'
# p1.sobrenome = 'Alberto'
print(p1.nome)
print(p1.sobrenome)