# 11. Remove given Element from Array

nums=[2,4,1,2,3,4,6,7,5,4]

target=4

# for num in nums:
#     if num==target:
#         nums.remove(num)

# print(nums)

ans=[i for i in nums if i!=target]

print(ans)