# 1. Reverse an Array

arr=[2,3,1,3,12]

# solution 1

i=0
j=len(arr)-1

while i<j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1

print(arr)

#solution 2

arr=arr[::-1]
print(arr)