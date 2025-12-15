'''
Task: Implement a singly linked list class with the following methods:
append(data): Adds a new node with the specified data at the end of the list.
prepend(data): Adds a new node with the specified data at the beginning of the list.
print_list(): Prints all the elements in the list.
'''
from mimetypes import inited


# Create a class for handling your Node functionality
class Node:
    def __init__(self, data):
        # Store the data values inside the node
        self.data = data
        # This is the pointer to the next node. It's currently set to None
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        #the head of the list, is currently empty
        self.head = None

    # Create append function below
    def append(self, data):
        #create a new node
        new_node = Node(data)
        # if the list is empty, the new node will become the head
        if self.head is None:
            self.head = new_node
            return
        current = self.head  # if list is not empty, will go through list and find last node
        while current.next:
            current = current.next # loop to keep pointing to next value in the list as long as there is value
        # set the last node next pointer to the new node
        current.next = new_node

    # Create Prepend function below
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        # update the head to be the new node
        self.head = new_node

    def print_list(self):
        current = self.head
        # loop until no nodes are left inside linked list
        while current:
            print(current.data)
            current = current.next

testing = SinglyLinkedList()
testing.append(10)
testing.append(20)
testing.append(30)
testing.prepend(5)

testing.print_list()