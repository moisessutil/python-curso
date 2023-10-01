lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

listaN = [55, 21, 2, 6, 3, 84, 10, 72]
listaN.sort()
print(listaN)
print('-' * 100)

# def ordena(item):
#     return item['nome']

lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for i in lista:
        print(i)

exibir(lista)

print('-' * 100)

l1 = sorted(lista, key=lambda item: item['sobrenome'])
exibir(l1)