# 19. Find Subarray with Given Sum.

arr=[1,4,5,9,5,3,4,6] 
k=19


i=0
curr=0

for j in range(len(arr)):
    curr+=arr[j]

    while curr>k:
        curr-=arr[i]
        i+=1

    if curr==k:
        print(arr[i:j+1])


