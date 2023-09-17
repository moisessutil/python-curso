salas = [['Gabriel', 'Jão'], ['Marcos'], ['Maria', 'José', (0, 10, 20, 30, 40)]]

print(salas[2][1])
print(salas[2][2][3])

print('-' * 100)

for sala in salas:
    for aluno in sala:
        print(aluno)