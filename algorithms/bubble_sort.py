def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(data)


data = [3, 64, 63, 1, 25, 2, 12, 22, 11]
bubbleSort(data)
print("Answer: ", data)
