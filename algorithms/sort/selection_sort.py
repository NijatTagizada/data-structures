'''
The selection sort algorithm sorts an array by repeatedly finding 
the minimum element (considering ascending order) from unsorted part
and putting it at the beginning. The algorithm maintains two subarrays in a given array.

Example:
arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64 
'''


def selection_sort(data):
    for i in range(len(data)):

        min_index = i
        for j in range(i + 1, len(data)):
            if data[min_index] > data[j]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]
        print(data)


data = [3, 64, 63, 1, 25, 2, 12, 22, 11]

selection_sort(data)
print('Answer: ', data)
