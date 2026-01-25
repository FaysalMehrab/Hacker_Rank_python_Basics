# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    n, m = map(int, input().split())
    
    # Top part
    for i in range(1, n, 2):
        pattern = '.|.' * i
        print(pattern.center(m, '-'))
    
    # Middle part    
    print('WELCOME'.center(m, '-'))
    
    for i in range(n-2, 0, -2):
        pattern = '.|.' * i
        print(pattern.center(m, '-'))
        
    
    
