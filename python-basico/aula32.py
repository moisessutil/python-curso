"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número: \n')

try:
    numero_int = int(numero)
    par_impar = numero_int % 2

    if par_impar == 0:
        print('Par!')
    else:
        print('Impar!')
    
except:
    print('Você não digitou um número inteiro')

print(100 * '-')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = float(input('Que horas são: \n'))

if hora > 0 and hora < 12:
    print('Bom dia!!!')
elif hora > 12 and hora < 18:
    print('Boa tarde!!!')
elif hora > 18 and hora < 24:
    print('Boa noite!!!')
else:
    print('Horario Inválido!')

print(100 * '-')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite o seu nome: \n')

nome_numero = len(nome)

if nome_numero <= 4:
    print('Seu nome é curto')
elif nome_numero > 4 and nome_numero <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')