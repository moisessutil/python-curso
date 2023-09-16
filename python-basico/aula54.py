lista = []

while True:
    print('Selecione uma opção')
    opcao = int(input('1 - Inserir\n2 - Apagar\n3 - Listar\n'))
    print('-' *100)

    if opcao == 1:
        item = input('Digite o item de deseja adicionar a lista:\n')
        lista.append(item)
        print('Item inserido')
        print('-' *100)

    elif opcao == 2:
        delete = int(input('Digite o indice da lista que deseja remover:\n'))
        del lista[delete]
        print('Item deletado')
        print('-' *100)

    elif opcao == 3:
        print('Lista de compras:')
        for num, item in enumerate(lista):
            print(num, item)
        print('-' *100)

    else:
        print('Opção invalida!')
