'''
Build a program that manages student records using a linked list. The user can add, search, delete, or display student information.
Students will implement a singly linked list where each node stores a student’s ID, name, and grade. The program should allow various operations using decision structures (menu-driven)
Steps:
Define a Student node structure/class with fields: ID, Name, Grade, and next.
Create a menu using if-else or switch statements:
1. Add Student
2. Search Student by ID
3. Delete Student
4. Display All Students
5. Exit
Implement each function:
Add: Insert a new node at the end.
Search: Traverse and check if the ID matches.
Delete: Adjust pointers to remove a node.
Display: Print all records.
Loop until the user chooses Exit.
'''

# Create a Student Class
class Student:
    def __init__(self, student_id, name, grade):
        # Store the student information inside the node
        self.student_id = student_id
        self.name = name
        self.grade = grade
        # This is the pointer to the next node. It's currently set to None
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        #the head of the list, is currently empty
        self.head = None

    # Add Student
    def append(self, student):
        # if the list is empty, the new node will become the head
        if self.head is None:
            self.head = student
            return
        #Otherwise, go through and find last node
        current = self.head
        while current.next:
            current = current.next # loop to keep pointing to next value in the list as long as there is value
        # set the last node next pointer to the new node
        current.next = student

    #Search Student by ID
    def search(self, student_id):
        current = self.head

        #Loop through the list
        while current:
            if current.student_id == student_id:
                #Student Found
                print("\nStudent Found!")
                print(f"\nStudent ID: {current.student_id}")
                print(f"Name: {current.name}")
                print(f"Grade: {current.grade}")
                return

            #Move to next node
            current = current.next

        #We got to the end of the loop and student was not found
        print("\nStudent could not be found.")

    #Delete Student
    def remove(self, student_id):
        #Look at the beginning of the list
        current = self.head
        previous = None

        #if list is empty
        if current is None:
            print("\nThere are no students found on the list.")
            return

        #if the node to remove is the head
        if current and current.student_id == student_id:
            #the list head moves to the next node
            self.head = current.next
            current = None  #old head removed
            print("\nStudent deleted.")
            return
        #if node to remove is not the head
        while current and current.student_id != student_id:
            #loop the list until data is found or until list ends
            previous = current
            current = current.next
        #if data is not found in the list
        if current is None:
            print(f"\nStudent with {student_id} not found.")
            return
        #Node to be removed is found and now 'current'
        #the 'previous' node skips 'current' and links to 'current.next'
        previous.next = current.next
        current = None # remove node
        print("\nStudent deleted.")

    #Display Students
    def print_list(self):
        current = self.head
        #If list is empty
        if current is None:
            print("\nNo students found on list.")
            return
        # loop to print each student on linked list
        while current:
            print("\n======Student Information===========")
            print(f"\nStudent ID: {current.student_id}")
            print(f"Name: {current.name}")
            print(f"Grade: {current.grade}")
            current = current.next
#Establishes a Main Menu
def main():

    #creates the empty linked list to store student information
    student_list = SinglyLinkedList()

    while True:
        print("\n====== STUDENT INFORMATION SYSTEM =========")
        print("\n1. Add Student")
        print("2. Search Student by ID")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()
        print()

        #Prompt user to input new student information
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student's Name: ")
            grade = input("Enter Student's Grade: ")

            #Calls the Student class creates a new student node
            student = Student(student_id, name, grade)

            #Adds the new student node to linked list
            student_list.append(student)
            print("\nStudent added successfully.")

         #Search Student by ID
        elif choice == '2':
            student_id = input("Enter Student ID to search: ")
            student_list.search(student_id)

        #Delete Student
        elif choice == '3':
            student_id = input("Enter Student ID to delete: ")
            student_list.remove(student_id)

        #Display All Students
        elif choice == '4':
            student_list.print_list()

        #Exit
        elif choice == '5':
            print("\nGoodbye!")
            exit()
        else:
            print("\nInvalid Option. Please enter a number between 1 and 5")
#Calls the main() function to pull up main menu
if __name__ == "__main__":
    main()