import string


def print_rangoli(size):
    # your code goes here
    al = string.ascii_lowercase
    width = size * 4 - 3
    lines = []
    
    for i in range(size):
        left = al[size-1:i:-1]
        right = al[i:size]
        line = '-'.join(left+right)
        lines.append(line.center(width, '-'))
        
    print('\n'.join(lines[::-1][:-1] + lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)