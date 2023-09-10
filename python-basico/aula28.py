nome = input('Digite o seu nome:\n')
idade = input('Digite a sua idade:\n')

if nome and idade:
    print(f'O seu nome é {nome}')
    print(f'O seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('O seu nome contém espaços')
    else:
        print('O seu nome não contém espaços')

    print(f'O seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')