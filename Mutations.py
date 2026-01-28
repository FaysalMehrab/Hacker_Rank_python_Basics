# 1st method: convert the string to a list and then change the value.

def mutate_string(string, position, character):
    
    str = list(string)
    
    str[position] = character
    
    return ''.join(str)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)



# 2nd method:  slice the string and join it back.

def mutate_string(string, position, character):
    
    string = string[:position] + character + string[position+1:]

    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)