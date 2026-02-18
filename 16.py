# 16. Check if Two Arrays Are Equal: if two arrays contain the same elements

arr1=[1,2,3,4,5,6]
arr2=[1,2,3,4,5,6]
i=0
flag=True

if len(arr1)!=len(arr2):
    print('Not equal')

else:
    while i<len(arr1):
        if arr1[i]!=arr2[i]:
            Flag=False
            break
        i+=1
    if flag==True:
        print("Equal")
    else:
        print("Not Equal")

    


