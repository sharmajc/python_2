"""
1. Explain the Merge Sort algorithm:  Merge Sort is a divide and conquer algorithm that takes an array, divides it in half
into a subarray and continues to divide the subarrays in half until subarray has 1 item.
Then the items are sorted as they are merged back together resulting in one final sorted list.
2. Demonstrate its implementation in Python to sort a list of strings in alphabetical order.
3. Give an example
"""

#2. Demonstrate Merge Sort implementation

def merge_sort(array):
    # check to see length of array.
    # If it is less than or equal to 1, then a list this small is already sorted.
    if len(array) <=1:
        return array

    mid = len(array)//2 # Finds the middle index by dividing the array into 2 halves

    left_half = array[:mid] # Left half contains all values in array up to, but not including mid

    right_half = array[mid:] # Right half contains all values from mid to the end of array

    #Recursion to merge_sort each half of array
    # Will split each subarray until base case of 1 element is reached.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge together sorted halves into one sorted list
    return merge(sorted_left, sorted_right)

#Merge function combines left and right sorted lists into one sorted list
def merge(left, right):
    result = []  # Empty list to store final sorted list
    i = j = 0 #Pointer for left list (i) and right list (j) index

    #Loop to compare items from both lists one at a time
    while i <len(left) and j < len(right): #keep running as long as both left and right lists has items in it
        #Compare lower case version of string so case does not affect sorting
        if left[i].lower() < right[j].lower(): #if current item in the left list (i) comes first alphabetically,
            result.append(left[i]) #add it to the result list
            i += 1 #move i pointer to next index
        else:
            result.append(right[j]) #Otherwise, add the item from the right list (j)
            j += 1 #move the j pointer to the next index

    #if there are leftover items in the left list, add them all to the result. They are already sorted.
    result.extend(left[i:])
    #if there are leftover items in the right list, add them all to the result
    result.extend(right[j:])

    return result

# 3. Example
#List of strings to sort alphabetically
produce = ["Carrots", "dragon fruit", "bananas", "eggplant", "apples"]
#calling merge_sort to sort list
sorted_produce = merge_sort(produce)

print("Sorted Produce:", sorted_produce)

