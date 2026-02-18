# 12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.

nums=[1,2,3,5,4,7,6,9]

total=0
n=len(nums)+1

for num in nums:
    total+=num

ans=((n*(n+1))//2) - total

print(ans)