from collections import OrderedDict

n = int(input())

od = OrderedDict()

for _ in range(n):
    
    *item_name_parts, item_price = input().split(' ')
    item_name =  ' '.join(item_name_parts)
    
    if item_name in od:
        od[item_name] += int(item_price)
    else:
        od[item_name] = int(item_price)
        
for item_name, item_price in od.items():
    print(f'{item_name} {item_price}')