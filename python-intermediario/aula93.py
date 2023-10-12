try:
    a = 19
    b = 0
    # print(b[0])
    c = a / b

# except ZeroDivisionError as erro:
#     print('Dividiu por zero!')
#     print('MSG:', erro)
#     print('NOME:', erro.__class__.__name__)

# except NameError as erro:
#     print('Nome não definido!')
#     print('MSG:', erro)
#     print('NOME:', erro.__class__.__name__)

except Exception as erro:
    print('NOME:', erro.__class__.__name__)
    print('MSG:', erro)