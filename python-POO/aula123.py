# escopo
class Animal:
    # nome = 'Zebra'

    def __init__(self, nome):
        self.nome = nome

        varialvel = 'valor'

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('carne'))