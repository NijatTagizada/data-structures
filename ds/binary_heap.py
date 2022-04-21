
'''
Heap data structure is a complete binary tree that satisfies the heap property, where any given node is

1) always greater than its child node/s and the key of the root node is the largest among all other nodes.
This property is also called max heap property.

2) always smaller than the child node/s and the key of the root node is the smallest among all other nodes.
This property is also called min heap property.

Examples of Min Heap:

            10                      10
         /      \               /       \  
       20        100          15         30  
      /                      /  \        /  \
    30                     40    50    100   40
    

Examples of Max Heap:
                     100
                  /       \  
                90         60
               /  \       /  \
             80    70    50    40
'''

def heapify(arr, size, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < size and arr[i] < arr[l]:
        largest = l
    
    if r < size and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, size, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
        
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)
    
arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))