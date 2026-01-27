if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for _ in range(N):
        s = input().split()
        cmd = s[0] 
        
        if cmd == 'append':
            
            lst.append(int(s[1]))
            
        elif cmd == 'insert':
            lst.insert(int(s[1]), int(s[2]))
        
        elif cmd == 'remove':
            lst.remove(int(s[1]))
            
        elif cmd == 'sort':
            lst.sort()
            
        elif cmd == 'pop':
            lst.pop()
            
        elif cmd == 'reverse':
            lst.reverse()
        else:
            print(lst)
            