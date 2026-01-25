n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    
    cmd = input().split()

    
    if cmd[0] == 'pop':
        if s:
            s.remove(min(s))
    elif cmd[0] == 'remove':
        s.discard(int(cmd[1]))
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))


print(sum(s))
