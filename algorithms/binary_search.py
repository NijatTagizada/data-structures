def binarySearch(arr, l, r, x):
    if r>=1:
        mid = 1+(r-1)//2
        
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l , mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)

arr = [2, 3, 4, 10, 40]

print(binarySearch(arr,0,len(arr),10))
