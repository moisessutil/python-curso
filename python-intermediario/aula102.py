# Variálveis livres + nonlocal

# def fora(x):
#     a = x
#     def dentro():
#         return a
#     return dentro

# dentro1 = fora(5)
# dentro2 = fora(6)

# print(dentro1())
# print(dentro2())

def concatenar(str_inicial):
    valor_final = str_inicial

    def interno(valor_concatenar):
        nonlocal valor_final
        valor_final += valor_concatenar
        return valor_final
    return interno

c = concatenar('a')
print(c('b'))