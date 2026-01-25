def int_div(a,b):
    return (a//b)

def float_div(a, b):
    return (a/b)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(int_div(a,b))
    print(float_div(a,b))
