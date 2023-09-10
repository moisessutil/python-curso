nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')


print(nome[2])
print('s' in nome)
print(100 * '-')
print('a' in nome)

print(100 * '-')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')