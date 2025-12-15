"""
What is the time complexity of the Quick Sort algorithm, and how would you implement it in Python?
Give an example
"""

def quicksort(array):
    # check to see if the list is already sorted
    if len(array) <=1:
        return array

    leader = array[len(array) // 2]
    left = [x for x in array if x < leader]
    middle = [x for x in array if x == leader]
    right = [x for x in array if x > leader]

    return quicksort(left)+ middle + quicksort(right)

numbers = [10, 7, 8, 9, 1, 5]
sorted_list = quicksort(numbers)

print("Sorted list:", sorted_list)
