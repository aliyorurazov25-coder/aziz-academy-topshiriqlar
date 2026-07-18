n = int(input()) 
max_num = float('-inf') 
for i in range(n): 
    num = int(input()) 
    if num > max_num: 
        max_num = num 
print(max_num)        