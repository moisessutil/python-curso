def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))