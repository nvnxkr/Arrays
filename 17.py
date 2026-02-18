# 17. Find the Leader Elements: An element is a leader if it is greater than all elements to its right.

arr=[16,17,4,3,5,2]
i=0
maxi=float('-inf')
ans=[]
for i in range(len(arr)-1,-1,-1):
    if arr[i]>maxi:
        ans.append(arr[i])

    maxi=max(maxi,arr[i])
ans.reverse()
print(ans)
