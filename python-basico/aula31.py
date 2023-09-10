"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = True
passou_no_if = None

if condicao:
    print('Faça algo')
    passou_no_if = True
else:
    print('Não faça nada')

print(passou_no_if is None)
print(passou_no_if is not None)

print(id(condicao))