# Python3 code to implement Jump Search
import math


def jumpSearch(arr , num , length):
	
	# Finding block size to be jumped
	step = math.sqrt(length)
	
	# Finding the block where element is
	# present (if it is present)
	prev = 0
	while arr[int(min(step, length)-1)] < num:
		prev = step
		step += math.sqrt(length)
		if prev >= length:
			return -1
	
	# Doing a linear search for x in
	# block beginning with prev.
	while arr[int(prev)] < num:
		prev += 1
		
		# If we reached next block or end
		# of array, element is not present.
		if prev == min(step, length):
			return -1
	
	# If element is found
	if arr[int(prev)] == num:
		return prev
	
	return -1

# Driver code to test function
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
	34, 55, 89, 144, 233, 377, 610 ]
number = 233
length = len(arr)

# Find the index of 'x' using Jump Search
index = jumpSearch(arr, number, length)

# Print the index where 'x' is located
print("Number" , number, "is at index" ,"%.0f"%index)
