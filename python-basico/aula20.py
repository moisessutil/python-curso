primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O valor de {primeiro_valor} é maior que {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O valor de {segundo_valor} é maior que {primeiro_valor}')
else:
    print('Os valores são identicos')