import json

CAMINHO_DO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Carlos', 35)
p2 = Pessoa('Paulo', 20)
bd = [p1.__dict__, p2.__dict__]

with open(CAMINHO_DO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)