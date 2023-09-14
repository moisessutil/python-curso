contador = 0

while contador <= 100:
    contador += 1

    if contador == 10:
        print(f'Não vou mostrar o {contador}')
        continue

    if contador >= 39 and contador <= 58:
        print(f'Não vou mostrar o {contador}')
        continue

    print(contador)

    if contador == 87:
        break

print('Acabou')