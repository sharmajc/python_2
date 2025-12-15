'''
Implement a basic queue using Python's built-in list data structure. The queue should support standard operations like enqueue, dequeue, and checking if the queue is empty.
Instructions:
Implement a class      Queue with the following methods:
enqueue(item): Adds an item to the end of the queue.
dequeue(): Removes and returns the item at the front of the queue. If the queue is empty, it should raise an exception.
is_empty(): Returns True if the queue is empty, False otherwise.
size(): Returns the number of items in the queue.
Write a few test cases to demonstrate the functionality of the queue.
'''

#create a class called a queue
class Queue:
    def __init__(self):
        #We will use this to store the elements inside the queue within a list
        self.items = []

    def enqueue(self, item):
        #Add items at the tail of the queue
        self.items.append(item)

    def dequeue(self):
        #Remove items from the front of the queue
        if self.is_empty():
            raise Exception("Queue is empty")
        # This will remove the first item from the queue
        return self.items.pop(0)

    def is_empty(self):
        # check if the list is empty
        return len(self.items) == 0

    def size(self):
        #check what's the length of the queue
        return len(self.items)

queue = Queue()

print("Is the queue empty: ", queue.is_empty())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Is the queue empty: ", queue.is_empty())
print("Size of your queue: ", queue.size())

print("Dequeued Item:", queue.dequeue())
print("Size of your queue: ", queue.size())

