from itertools import product

A = list(map(int, input().split()))

B = list(map(int, input().split()))

pd = product(A, B)

for i in pd:
    print(i, end = ' ')
