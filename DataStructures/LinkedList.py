# Linked List
"""
Linked List is a Linear Data Structure
Linked List elements are not stored at contiguous memory location
The elements are linked using pointers
This includes a series of connected Nodes
Each Node stores  the Data and address of the next Node
There are 3 types of Linked List
1] Singly Linked List
2] Doubly Linked List
3] Circular Linked List : If the last Node in the Linked List contains the address of the head Node then
                          it is a Circular Linked List
                          Circular Linked List are also of 2 types
                          1] Singly Circular Linked List : The methods are same as Singly Linked List
                          2] Doubly Circular Linked List : The methods are same as Doubly Linked List
"""

'''
# Advantages of Linked Lists
Linked List are Dynamic in Size
No wastage as Capacity and size is always equal
Easy insertion and deletion as 1 or 2 Link Manipulation is required
Efficient Memory allocation 
'''

'''
# Disadvantages of Linked Lists
If Head Node is lost , Linked List is lost
No Random access is Possible
'''

# Singly Linked List
'''
In Singly Linked List Insertion and Deletion can be done at the Beginning,
at Specific or at the End
Traversal is only done one way 
'''


# Implementing Singly Linked List in Python
# First we need to create Node class to store data and address of the next Node
class Node:
    # Initializing the Node
    def __init__(self, data):
        self.data = data
        self.next = None


# After creating Node class we need to create Singly Linked List class
# This class will contain Node objects
class SinglyLinkedList:
    # Initializing the Head of the Singly Linked List
    def __init__(self):
        self.head = None
        self.length = 1

    # Function to add new Node at the end of Singly Linked List
    def append_node(self, data):
        new_node = Node(data)
        temp = self.head

        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.next = None
        self.length += 1

    # Function to add new Node at the start of the Singly Linked List
    def prepend_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # Function to add new Node at a given position in the Singly Linked List
    def insert_node(self, position, data):
        new_node = Node(data)
        temp = self.head
        if position > self.length:
            self.append_node(data)
        else:
            for i in range(0, position - 1):
                temp = temp.next
            current_node = temp
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    # Function to remove Node at the given position in the Singly Linked List
    def remove_node(self, position):
        if position < 0 or position > self.length:
            print('Node does not exist at ' + str(position))
            return None

        if position == 0:
            temp = self.head.next
            self.head = temp
            self.length -= 1
            return None

        temp = self.head
        node_to_remove = temp.next

        for i in range(0, position - 1):
            temp = temp.next
            node_to_remove = node_to_remove.next

        next_node = node_to_remove.next
        node_to_remove.next = None
        temp.next = next_node
        self.length -= 1

    # Function to print all the Nodes in the Singly Linked List
    def print_nodes(self):
        if self.head is None:
            print('Singly Linked List is Empty!')
        else:
            temp = self.head
            while temp is not None:
                if temp.next is not None:
                    print(temp.data, end='->')
                else:
                    print(temp.data)
                temp = temp.next

    # Function to print the Length of the Singly Linked List
    def show_length(self):
        print(f'\n{self.length}')


'''
We can initialize the SinglyLinkedList class i.e SinglyLinkedList()
After initializing the SinglyLinkedList class we need to create a Node
and assign it to the head of the SinglyLinkedList i.e SinglyLinkedList.head = Node(1)
We can use methods in SinglyLinkedList class to manipulate the SinglyLinkedList
'''

# Doubly Linked List Questions

# Question 1
'''
You're given a Linked List print the Middle element of the LinkedList
Input : [1, 2, 3, 4, 5]
Output : 3
Leetcode link https://leetcode.com/problems/middle-of-the-linked-list/
'''


def get_middle_node(linked_list):
    # Two pointer approach
    slow_pointer = linked_list.head
    fast_pointer = slow_pointer.next

    while fast_pointer.next is not None:
        fast_pointer = fast_pointer.next
        if fast_pointer.next is not None:
            fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next


# Question 2
'''
You're given a Linked List. Reverse the given Linked List and print it
Input : [1, 2, 3, 4, 5]
Output : [5, 4, 3, 2, 1]
Leetcode link https://leetcode.com/problems/reverse-linked-list/
'''


def reverse(linked_list):
    prev_node = None
    curr_node = linked_list.head

    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    linked_list.head = prev_node
