def count_substring(string, sub_string):
    count = 0
    sub_string_len = len(sub_string)
    for i in range(len(string)):
        if string[i:sub_string_len] == sub_string:
            count += 1
        else:
            pass
        sub_string_len += 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)