'''
Reverse a Singly Linked List using Recursion -
Choose your own list and reverse it recursively
'''

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

    # Append a value to the end of the list
    def append(self, data):
        #create a new node
        new_node = Node(data)

        # if the list is empty, the new node will become the head
        if self.head is None:
            self.head = new_node
            return
        current = self.head # if list is not empty, will go through list and find last node
        while current.next:
            current = current.next # loop to keep pointing to next value in the list as long as there is value
        # set the last node next pointer to the new node
        current.next = new_node

    # Prepend Function - add value to beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        # update the head to be the new node
        self.head = new_node

    # Prints all the values in the linked list
    def print_list(self):
        current = self.head
        # loop until no nodes are left inside linked list
        while current:
            print(current.data)
            current = current.next

    #Reversal of list Using recursion
    def reverse_list(self, node):
        #base case - if current node is empty or the last node,
        # current node becomes the new head of the reversed list.
        if node is None or node.next is None:
            return node

        #recursvie case
        new_head = self.reverse_list(node.next) #Reverse the rest of the list starting from node.next

        node.next.next = node #Reverse the pointer and make next node point back to current node

        node.next = None  #free the old pointer

        return new_head #return the new head for reversed list

    # Reverses the list when called
    def reverse(self):
        self.head = self.reverse_list(self.head)

#========TESTING===========

#Creating singly linked list and adding values
testing = SinglyLinkedList()
testing.append(10)
testing.append(15)
testing.append(20)
testing.append(25)
testing.prepend(5)

print("Original List:")
testing.print_list()
print('*****************************')

#Reversing the list
testing.reverse()

print("Reversed List:")
testing.print_list()


