import random

for _ in range(100):
    cpf = ''

    for i in range(11):
        cpf += str(random.randint(0, 9))

    nove_digitos = cpf[:9]
    contador1 = 10
    soma1 = 0
    soma2 = 0

    for numero in nove_digitos:
        soma1 += int(numero) * contador1
        contador1 -= 1

    resultado1 = (soma1 * 10) % 11
    resultado1 = resultado1 if resultado1 <= 9 else 0

    dez_digitos = nove_digitos + str(resultado1)

    contador2 = 11

    for numero in dez_digitos:
        soma2 += int(numero) * contador1
        contador2 -= 1

    resultado2 = (soma2 * 10) % 11
    resultado2 = resultado2 if resultado2 <= 9 else 0

    comparador1 = int(cpf[9])
    comparador2 = int(cpf[10])

    if resultado1 == comparador1 and resultado2 == comparador2:
        print(f'O CPF {cpf} válido')
        print('-' * 100)
    else:
        print(f'O CPF {cpf} inválido')
        print('-' * 100)