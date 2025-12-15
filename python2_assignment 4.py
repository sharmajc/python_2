'''
Use Python's collections.deque to implement a more efficient queue.
Instructions:
Implement a class DequeQueue with the following methods:
enqueue(item): Adds an item to the end of the queue.
dequeue(): Removes and returns the item at the front of the queue. If the queue is empty, it should raise an exception.
is_empty(): Returns True if the queue is empty, False otherwise.
size(): Returns the number of items in the queue.
Write a few test cases to demonstrate the functionality of the queue.
'''
from collections import deque

#create a class called a queue
class DequeQueue:
    def __init__(self):
        #We will use this to store the elements inside the queue within a list
        self.items = deque()

    def enqueue(self, item):
        #Add items at the tail of the queue
        self.items.append(item)

    def dequeue(self):
        #Remove items from the front of the queue
        if self.is_empty():
            raise Exception("Queue is empty")
        # This will remove the first item from the queue
        return self.items.popleft()

    def is_empty(self):
        # check if the list is empty
        return len(self.items) == 0

    def size(self):
        #check what's the length of the queue
        return len(self.items)

#create a queue instance
queue = DequeQueue()

print("Is the queue empty: ", queue.is_empty())

#add items into the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

#check if the queue is empty
print("Is the queue empty: ", queue.is_empty())
#Get the size of the queue
print("Size of your queue: ", queue.size())

#Dequeue an element from the queue
print("Dequeued Item:", queue.dequeue())
print("Size of your queue: ", queue.size())


