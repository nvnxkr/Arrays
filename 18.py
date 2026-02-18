# 18. Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.

arr=[0,1,0,3,12,0,2,3,4,5,0]

i=0
j=1

while j<len(arr) and i<len(arr):
    if arr[i]==0 and arr[j]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j+=1
    elif arr[i]!=0:
        i+=1
    elif j<i:
        j=i+1
    else:
        j+=1

print(arr)
