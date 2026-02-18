# 20. Rotate Array to the Left by k Positions

arr=[1,2,3,4,5,6,7,8]
k=3

# new=arr[k:]+arr[:k]
# print(new)

def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

reverse(arr,0,k-1)
reverse(arr,k,len(arr)-1)
reverse(arr,0,len(arr)-1)

print(arr)