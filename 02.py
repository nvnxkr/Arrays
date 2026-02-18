# 2. Find the Maximum & Minimum Element of an array

nums=[2,10,9,8,6,21,1]

mini=nums[0]
maxi=nums[0]

for num in nums:
    if num<=mini:
        mini=num
    if num>=maxi:
        maxi=num

print(f'Maximum is {maxi}')
print(f'Minimum is {mini}')
