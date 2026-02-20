# 24. Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.

arr = [1, 2, 3, 4, 5, 6]  #output=[6, 1, 5, 2, 4, 3]
i=0
j=len(arr)-1

ans=[]
arr.sort()

while i<j:
    ans.append(arr[j])
    ans.append(arr[i])
    j-=1
    i+=1
print(ans)