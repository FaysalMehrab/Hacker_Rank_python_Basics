n = int(input())

n_e = set(map(int, input().split()))

b = int(input())

b_e = set(map(int, input().split()))

r = n_e.difference(b_e)

print(len(r))
