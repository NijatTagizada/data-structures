
'''
Like QuickSort, Merge Sort is a Divide and Conquer algorithm.
It divides the input array into two halves, calls itself for the two halves, 
and then merges the two sorted halves. The merge() function is used for merging two halves. 
The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and
merges the two sorted sub-arrays into one
'''

def merge_sort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        merge_sort(L)
  
        # Sorting the second half
        merge_sort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            

data = [3, 64, 63, 1, 25, 2, 12, 22, 11]
merge_sort(data)
print("Answer: ", data)