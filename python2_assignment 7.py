"""
How would you implement the Bubble Sort algorithm in Python to sort a list of numbers in ascending order?
Give an example
"""

def bubbles(array):
    number = len(array)

    #we will be creating a nested loop to do the bubble sorting for the elements
    for i in range(number):
        for j in range(0,number - i - 1):
            #here we will be doing the swaps for elements
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

list_testing = [90, 64, 34, 25, 12, 22, 11]
sorted_list = bubbles(list_testing)

print("Sorted List: ", sorted_list)