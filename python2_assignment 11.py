'''
Implement a binary search tree (BST) and include methods for inserting nodes and searching for a value.
Instructions:
Implement a class Node that represents a node in the BST.
Implement a class BinarySearchTree that supports inserting nodes and searching for a value.
Write test cases to verify the implementation.
'''

# Create a Node class to represent a node in BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create a BinarySearchTree Class to support insertion and searching
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new value into the tree
    def insert(self, value):
        if self.root is None:  #If tree is empty,
            self.root = Node(value) # the first inserted value becomes the root
        else:
            self.recursive_insertion(self.root, value) #Otherwise use the recursive function to place it in correct spot

    # Helper function for insertion
    def recursive_insertion(self, current, value):
        # If the new value is smaller, it go left
        if value < current.value:
            if current.left is None: #if left child is empty,
                current.left = Node(value) #insert value here
            else:
                self.recursive_insertion(current.left, value) #Otherwise, continue left
        # If the new value is greater or equal, go right
        else:
            if current.right is None:  #if right child is empty,
                current.right = Node(value) #insert value here
            else:
                self.recursive_insertion(current.right, value) #Otherwise, continue right

    # Search for a value in the BST
    def search(self, value):
        # Start search at root node
        return self.recursive_search(self.root, value)

    # Helper Function for search
    def recursive_search(self, current, value):
        # Base Case: Value not found in tree
        if current is None:
            return False

        if current.value == value: #If current node matches value,
            return True # Value is Found!

        # If value is smaller, search left child
        if value < current.value:
            return self.recursive_search(current.left, value)

        #Otherwise, search right child
        else:
            return self.recursive_search(current.right, value)

    #=========TESTING============
tree = BinarySearchTree()

# Inserting values
tree.insert(50)
tree.insert(10)
tree.insert(60)
tree.insert(30)
tree.insert(20)
tree.insert(40)

# Searching Values (True = Found; False = Not Found)
print("Searching for 60:", tree.search(40))
print("Searching 30:", tree.search(20))
print("Searching for 90:", tree.search(85))
print("Searching for 75", tree.search(75))