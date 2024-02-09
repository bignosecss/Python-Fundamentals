import random

l = []

for i in range(10):
    l.append(random.randint(1, 10))

for n in l:
    if n % 2 == 0:
        n = 0
    print(n, end="\t")
