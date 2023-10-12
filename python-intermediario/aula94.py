# try, except, else e finally

try:
    print('Olá')
    10/0
except Exception as erro:
    print('NOME:', erro.__class__.__name__)
    print('MSG:', erro)
finally:
    print('Saiu!')