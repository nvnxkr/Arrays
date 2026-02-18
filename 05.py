# 5. Count Frequency of Elements

nums=[1,3,2,2,3,4,1,2,3,2,3,4,5]
freq={}

for num in nums:
    freq[num]=freq.get(num,0)+1

for k,v in freq.items():
    print(f'{k} --> {v} times')

