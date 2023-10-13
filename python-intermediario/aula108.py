# count

from itertools import count

c1 = count(0, 8)

for i in c1:
    if i >= 100:
        break

    print(i)