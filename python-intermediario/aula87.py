lista = ['a', 1, 2.5, True, [0, 1, 2, 3], (1, 2), {1, 2}, {'nome' : 'Carlos'}]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item)

    if isinstance(item, (int, float)):
        print(item)