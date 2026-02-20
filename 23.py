# 23. Maximum Sum Subarray (Kadane's Algorithm)

arr=[1,4,-5,9,4,-20,5,6]
print(sum(arr))
res=arr[0]
max_sum=arr[0]

for i in range(1,len(arr)):
    max_sum=max(max_sum+arr[i],arr[i])

    res=max(res,max_sum)

print(res)