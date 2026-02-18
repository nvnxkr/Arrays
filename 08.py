# 8. Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.

nums=[1,4,3,2,3,6,4,7,8,4]
target=10

i=0
j=len(nums)-1

nums.sort()

while i<j:
    if nums[i]+nums[j]==target:
        print([nums[i],nums[j]])
        i+=1
        j-=1
    elif nums[i]+nums[j]>target:
        j-=1
    else:
        i+=1

    
    