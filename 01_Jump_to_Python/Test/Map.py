n = 5
arr1=[9,20,28,18,11]
arr2=[30,1,21,17,28]

ans=[]

for i in range(0, n):
    arr1[i] = bin(arr1[i])
    arr2[i] = bin(arr2[i])
print(list(arr1[1]))
