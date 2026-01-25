def minion_game(string):
    # your code goes here
    vowel = 'AEIOUaeiou'
    k_s = 0
    s_s = 0
    l = len(string)
    
    for i in range(l):
        if string[i] in vowel:
            k_s += l - i
        else:
            s_s += l - i
    
    
    if (k_s > s_s):
        print('Kevin', k_s)
    elif(s_s > k_s):
        print('Stuart', s_s)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)