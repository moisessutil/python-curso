lista = [123, True, 'Cleitom', 1.45]

print(lista)

lista[3] = 'Siiiii'

print(lista[3])

del lista[3] # deleta um indice especifico

nome = 'Pedro'

lista.append(nome) # adiciona no final da lista

print(lista)

lista.pop(1) # remove o ultimo elemento ou algum elemento escolhido

lista.insert(0, 50) # insere em qualquer lugar da lista

print(lista)

lista.clear() # limpa a lista

lista_a = [1, 2, 3, 4]
lista_b = [5, 6, 7, 8]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)

print(lista_c)
print(lista_a)