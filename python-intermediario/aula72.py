def mult(*args):
    total, *resto = args

    for i in resto:
        total *= i 
    
    return total

def par_impar(i):
    resto = i % 2

    if resto == 0:
        return f'{i} é par!'
    else:
        return f'{i} é impar!'

multi = mult(3, 3, 12, 11, 9)
print(multi)
print(3 * 3 * 12 * 11 * 9)

print(par_impar(6))