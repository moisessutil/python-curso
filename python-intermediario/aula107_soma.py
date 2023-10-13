l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

lista_soma = [
    x + y 
    for x, y in zip(l1, l2)
]

# for i in range(min(len(l1), len(l2))):
#     lista_soma.append(l1[i] + l2[i])

print(lista_soma)