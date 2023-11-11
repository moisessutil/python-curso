class Pessoa:
    cpf = 1234

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    cpf = 'cpf aluno'

c1 = Cliente('André', 'Souza')
c1.falar_nome_classe()
a1 = Aluno('José', 'Filho')
a1.falar_nome_classe()
print(a1.cpf)
print(c1.cpf)

