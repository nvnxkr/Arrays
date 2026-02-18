# 10. Merge Two Sorted Arrays

arr1=[1,3,5,7]
arr2=[2,4,5,5,6,8,11,13]

i=0
j=0

ans=[]

while i<len(arr1) and j<len(arr2):
    if arr1[i]<=arr2[j]:
        ans.append(arr1[i])
        i+=1
    else:
        ans.append(arr2[j])
        j+=1

while i<len(arr1):
    ans.append(arr1[i])
    i+=1

while j<len(arr2):
    ans.append(arr2[j])
    j+=1

print(ans)

    
