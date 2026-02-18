# 14. Find Intersection of Two Arrays: Find the common elements between two arrays.
arr1=[1,2,3,4,5,6]
arr2=[4,5,6,7,2,3,8,9]
i=0
j=0
inter=[]
arr1.sort()
arr2.sort()

while i<len(arr1) and j<len(arr2):
    if arr1[i]==arr2[j]:
        inter.append(arr1[i])
        i+=1
        j+=1
    elif arr1[i]<arr2[j]:
        i+=1
    else:
        j+=1

print(inter)


