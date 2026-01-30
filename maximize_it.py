from itertools import product

def maximize_it(list_item, m):
    
    output = 0
    
    for items in product(*list_item):
        temp = 0
        
        for item in items:
            temp += item ** 2
            
        temp = temp % m
        
        if temp > output:
            
            output = temp
            
    return output
    



k, m = input().split()

n_list = []

for i in range(int(k)):
    n = list(map(int, input().split()))
    n_list.append(n[1:])
    

output = maximize_it(n_list, int(m))

print(output)
    