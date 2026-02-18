# 4. Find the Second Largest Element
nums=[0,2,3,42,13,53,66,44,54]

largest=nums[0]
s_largest=None

for num in nums:
    if num<largest and num>s_largest:
        s_largest=num

    elif largest<num:
        s_largest=largest
        largest=num

print(f'second largest is {s_largest} ')

