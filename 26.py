# 26. Find Peak Element: A peak element is greater than its neighbors. Find one such element.

arr=[1,5,4,6,3,4,5,9,10,11]

def peak(arr):
    for i in range(len(arr)-1):
        if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
            print(arr[i]) 

peak(arr)