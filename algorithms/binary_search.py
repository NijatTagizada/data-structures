def binary_search(list, n):  
    low = 0  
    high = len(list) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list[mid] < n:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif list[mid] > n:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  


def binary_search_recursive(list1, low, high, n):   
  
   # Check base case for the recursive function  
   if low <= high:  
  
      mid = (low + high) // 2  
  
      # If element is available at the middle itself then return the its index  
      if list1[mid] == n:   
         return mid   
  
      # If the element is smaller than mid value, then search moves  
      # left sublist1  
      elif list1[mid] > n:   
         return binary_search_recursive(list1, low, mid - 1, n)   
  
      # Else the search moves to the right sublist1  
      else:   
         return binary_search_recursive(list1, mid + 1, high, n)   
  
   else:   
      # Element is not available in the list1  
      return -1  



arr = [2, 3, 4, 10,15,22,24 ]


print('Answer: ', binary_search(arr, 231))
print('Answer: ', binary_search_recursive(arr,0,len(arr),22))
