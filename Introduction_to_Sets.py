def average(array):
    d_h = set(array)
    
    return sum(d_h)/len(d_h)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)