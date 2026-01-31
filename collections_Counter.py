from collections import Counter

num_shoes = int(input())

shoe_avail = list(map(int,input().split()))

cus_num = int(input())

shoe_counter = Counter(shoe_avail)

t_money = 0

for i in range(cus_num):
    
    size, price = map(int, input().split())
    
    if shoe_counter[size] > 0:
        
        t_money += price
        
        shoe_counter[size] -= 1
        
print(t_money)