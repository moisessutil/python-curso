import os

palavra = 'perfume'
letra_acertada = ''
tentativas = 10
contador = 0

while True:
    print(f'Você tem {tentativas} tentativas')
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue
    
    contador += 1

    if letra in palavra:
        letra_acertada += letra

    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(palavra_formada)

    if palavra_formada == palavra:
        os.system('cls')
        print('Você ganhou!!!')
        print(f'A palavra era {palavra_formada}')
        print(f'Você realizou {contador} tentativas')
        letra_acertada = ''
        tentativas = 10
        contador = 0

    if tentativas == 1:
        os.system('cls')
        print('Você esgotou sua tentativas :(')
        seguir = int(input('Digite 1 para continuar e 2 para sair: '))

        if seguir == 1:
            letra_acertada = ''
            tentativas = 10
            contador = 0
            continue
        elif seguir == 2:
            break
        else:
            print('Opção invalida')

    tentativas -= 1