# 15. Find Union of Two Arrays

arr1=[1,2,3,4,5,6]
arr2=[4,5,6,7,2,3,8,9]
i=0
j=0
union=[]
arr1.sort()
arr2.sort()

for i in arr1:
    union.append(i)

for j in arr2:
    if j not in union:
        union.append(j)

print(union)
