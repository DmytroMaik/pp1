arr = [-15, 8, -31, 47, -2, 19]
max = arr[0] 
min = arr[0]
for i in range(len(arr)):
    if i > max:
        max = arr[i]

for i in range(len(arr)):
    if arr[i] < max:
        min = arr[i]

print(max)
print(min)


    
