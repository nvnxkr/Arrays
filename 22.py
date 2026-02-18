# 22. Find All Subarrays
arr=[1,2,3,4]

i=0
j=0

all=[]
temp=[]

for i in range(len(arr)):
    for j in range(i,len(arr)):
        print(arr[i:j+1])
