numero_str = input('Digite um número: ')

try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')