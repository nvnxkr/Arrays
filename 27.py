# 27. Find the First Missing Positive: Find the smallest positive integer missing in the array. 

arr = [3, 4, -1, 1]
mini=1

for i in range(1,len(arr)+2):
    if i not in arr:
        print(i)
        break

