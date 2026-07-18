n = int(input()) 
min_num = float('inf') 
for i in range(n): 
    num = int(input()) 
    if num < min_num: 
        min_num = num 
print(min_num)        