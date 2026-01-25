# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

s = [input().strip() for _ in range (n)]

count = {}

for word in s:
    if word in count:
        count[word] += 1
    else:
        count[word] =1
        
print(len(count))

print(*count.values())