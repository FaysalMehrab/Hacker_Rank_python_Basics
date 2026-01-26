if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
    st = sorted(set(arr))
    
    print(st[-2])
    
    