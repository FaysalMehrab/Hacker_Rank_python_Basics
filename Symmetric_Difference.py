# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))
    
s_d = a ^ b

for i in sorted(s_d):
    print(i)