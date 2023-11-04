class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def pessoa_50_anos(cls, nome):
        return cls(nome, 50)
    
p1 = Pessoa('Jão', 35)
p2 = Pessoa.pessoa_50_anos('Carlos')
print(p2.nome, p2.idade)