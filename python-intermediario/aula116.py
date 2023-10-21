# arquivos

caminho_arquivo = 'C:\\Users\\moise\\OneDrive\\Documents\\Estudos\\python-curso\\python-intermediario\\'
caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Ola Mundo\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )

with open(caminho_arquivo, 'a+') as arquivo:
    arquivo.write('Ola Mundo\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())