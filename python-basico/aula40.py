condicao = True
contador = 1

while condicao:
    operacao = int(input('Qual operação deseja realizar:\n1 - adição\n2 - subtração\n3 - divisão\n4 - multiplicação\n'))

    if operacao == 1:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite um número: '))
        res = n1 + n2
        print(f'O resultado da soma de {n1} e {n2} da {res}')
        condicao = False

    elif operacao == 2:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite um número: '))
        res = n1 - n2
        print(f'O resultado da subtração de {n1} e {n2} da {res}')
        condicao = False

    elif operacao == 3:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite um número: '))
        res = n1 / n2
        print(f'O resultado da divisão de {n1} e {n2} da {res}')
        condicao = False

    elif operacao == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite um número: '))
        res = n1 * n2
        print(f'O resultado da soma de {n1} e {n2} da {res}')
        tab = input('Deseja saber alguma tabuada? ')

        if tab == 'sim':
            tab1 = float(input('Digite qual tabuada você deseja saber: '))
            tab2 = int(input('Até qual tabuada você deseja ir: '))
            contador2 = 1

            while contador2 <= tab2:
                print(f'{tab1} * {contador2} = {tab1 * contador2}\n')
                contador2 += 1

        condicao = False

    else:
        print('Número ou caracter inválido')