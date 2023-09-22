x = 1


def escopo():
    global x
    x = 10
    print(x)

    def outra_funcao():
        x = 11
        print(x)

    outra_funcao()

print(x)
escopo()
print(x)