# 13. Find Duplicates in an Array
arr=[1,2,3,4,5,6,7,1,2,1,2,3]

freq={}

for num in arr:
    freq[num]=freq.get(num,0)+1

for k,v in freq.items():
    if v>1:
        print(f'{k} appears {v} times')

    