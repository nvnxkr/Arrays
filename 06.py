# 6. Check if Array is Sorted

nums=[2,3,6,7,8,10]
flag=True
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        flag=False
        break

if flag:
    print('Sorted array')
else:
    print('Not Sorted')


        