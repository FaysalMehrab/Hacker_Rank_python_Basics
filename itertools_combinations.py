from itertools import combinations

string_input = input().split()

st = ''.join(sorted(string_input[0]))
n = int(string_input[1])


for i in range(1, n+1):
    for c in combinations(st, i):
        print(''.join(c))
