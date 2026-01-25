# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())

n_a = list(map(int, input().split()))

m_a = set(map(int, input().split()))
m_b = set(map(int, input().split()))

count = 0

for i in n_a:
    if i in m_a:
        count += 1
    elif i in m_b:
        count -= 1
        
print(count)  