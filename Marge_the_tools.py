def merge_the_tools(string, k):
    # your code goes here
    sub_string = [string[i : i+k] for i in range(0, len(string), k)]
    
    for i in sub_string:
        print(''.join(map(str, set(i))))
    
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)