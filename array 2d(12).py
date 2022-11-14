arr = [[2,3,4],[9,0,3]]
#a
print(arr)
#b
print(len(arr), len(arr[0]))
#c
print(arr[0][1])
#d
print(arr[1][2])
#e
print(arr[1])
#f
#print(arr[0],arr[1])
for i in arr:
    print (i)
#g
for i in arr:
    print(i[len(i)-1])