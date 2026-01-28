# This a O(n^2)

def swap_case(s):
    st = ''
    for ch in s:
        if ch.isupper():
            st += ch.lower()
        elif ch.islower():
            st += ch.upper()
        else:
            st += ch     
        
    return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# This is O(n) - better approach

def swap_case(s):
    result = []
    for ch in s:
        if ch.isupper():
            result.append(ch.lower())
        elif ch.islower():
            result.append(ch.upper())
        else:
            result.append(ch)     
        
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)