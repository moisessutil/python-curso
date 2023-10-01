import copy

pessoa = {
    'nome' : 'Cleitom',
    'sobrenome' : 'Rasta',
    'idade' : 65,
    'altura' : 1.60,
    'enderecos' : [
        {'rua' : 'Foda-se', 'numero' : 157}
    ],
}

# pessoa.setdefault('idade', 0)
# print(len(pessoa)) # retorna a quantiade de chaves

# print(list(pessoa.keys())) # retorna as chaves
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# print(pessoa['idade'])

d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [1,2,3]
}

# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 10000
# print(d1)
# print(d2)

p1 = {
    'nome' : 'Carlos',
    'sobrenome' : 'Silva'
}

# print(p1.get('nome'))

# nome = p1.pop('nome')
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(nome)

p1.update(nome='novo valor', idade=30)
print(p1)