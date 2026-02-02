A = int(input())

A_E = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    
    cmd, _ = input().split()
    
    n_e = set(map(int, input().split()))
    
    if cmd == 'update':
        A_E.update(n_e)
    elif cmd == 'intersection_update':
        A_E.intersection_update(n_e)
    elif cmd == 'difference_update':
        A_E.difference_update(n_e)
    elif cmd == 'symmetric_difference_update':
        A_E.symmetric_difference_update(n_e)


print(sum(A_E))