
# Need to switch to python 2 for this challenge
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = tuple(integer_list)
    
    print(hash(t))