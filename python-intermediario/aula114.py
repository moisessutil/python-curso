# função recursiva
# import sys

# sys.setrecursionlimit(2004)

# def recursiva(inicio=0, fim=10):
#     print(inicio, fim)

#     if inicio >= fim:
#         return fim

#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva(0, 2000))

def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n - 1)

print(fatorial(6))