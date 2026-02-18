# 7. Rotate Array by k Positions: Rotate the array to the right by k positions.

nums=[1,2,3,4,5,6,7]
k=3

nums=nums[3:]+nums[:3]

print(nums)