def soma(*args):
    total = 0

    for i in args:
        total += i

    print(total)

soma(1, 2, 3, 89, 1045, 873)

print(sum((1, 2, 3, 89, 1045, 873)))