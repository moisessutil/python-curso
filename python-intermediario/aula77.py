pessoa = {}

chave = 'nome'
pessoa[chave] = 'Pedro'
pessoa['sobrenome'] = 'Silva'

print(pessoa[chave])
print(pessoa['sobrenome'])

del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])