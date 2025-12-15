'''
Removing a Node from a Singly Linked List
====================================
Task: Implement a method remove(data) in the LinkedList class
that removes the first occurrence of a node with the specified data from the list.
'''

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

    #Remove data method inside singly linked class
    def remove(self, data):
        #Look at the beginning of the list
        current = self.head
        previous = None
        #if the node to remove is the head
        if current and current.data == data:
            #the list head moves to the next node
            self.head = current.next
            current = None  #old head removed
            return
        #if node to remove is not the head
        while current and current.data != data:
            #loop the list until data is found or until list ends
            previous = current
            current = current.next
        #if data is not found in the list
        if current is None:
            print(f"Node with {data} not found.")
            return
        #Node to be removed is found and now 'current'
        #the 'previous' node skips 'current' and links to 'current.next'
        previous.next = current.next
        current = None # remove node

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
testing.remove(10)

testing.print_list()