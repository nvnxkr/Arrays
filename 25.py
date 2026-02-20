# 25. Find Majority Element: Find the element that appears more than n/2 times.

arr=[2,2,2,3,4,5,2,2]

# arr.sort()

# print(arr[len(arr)//2])
freq={}

for num in arr:
    freq[num]=freq.get(num,0)+1

for k,v in freq.items():
    if v>len(arr)//2:
        print(k)
else:
    print("no majority element")