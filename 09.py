# 9. Remove Duplicates from Array: Remove duplicates from the array while maintaining order.
#assuming that the numbers is in sorted

nums=[2,3,3,4,4,4,5,5,6]

ans=[]

# for num in nums:
#     if num not in ans:
#         ans.append(num)

# print(ans)

i=0
for j in range(1,len(nums)):
    if nums[i]!=nums[j]:
        i+=1
        nums[i]=nums[j]

print(nums[:i+1])