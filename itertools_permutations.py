from itertools import permutations

string_input = input().split()

st = str(string_input[0])

n = int(string_input[1])

permutation = list(permutations(st, n))

permutation.sort()

for i in permutation:
    
    print(''.join(i))
