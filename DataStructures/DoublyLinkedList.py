# Doubly Linked List
"""
Doubly Linked List is similar to Singly Linked List
Only difference Doubly Linked List have is Two pointers Prev_pointer and Next_pointer
Prev_pointer has the address of the previous Node and Next_pointer has the address of the next Node
Traversal is done both way Forward and Backward
"""


# Implementing Doubly Linked List in Python
# Similar to the Linked List we need Node class to store data and addresses of the next and previous Nodes
class Node:
    # Initializing the Node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    # Initializing the head of Doubly Linked List
    def __init__(self):
        self.head = None
        self.length = 1

    # Function to add the Node at the end of Doubly Linked List
    def append_node(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        self.length += 1

    # Function to add the Node at the Beginning of Doubly Linked List
    def prepend_node(self, data):
        new_node = Node(data)
        temp = self.head
        temp.prev = new_node
        new_node.next = temp
        self.head = new_node
        self.length += 1

    # Function to add the Node at the give position in the Doubly Linked List
    def insert_node(self, data, position):
        new_node = Node(data)
        temp = self.head

        for i in range(0, position):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        self.length += 1

    # Function to remove the Node at the given position in the Doubly Linked List
    def remove_node(self, position):
        if position < 0 or position > self.length:
            print('Node does not exist at ' + str(position))
            return None

        if position == 0:
            new_head = self.head.next
            head = self.head
            head.next = None
            new_head.prev = None
            self.head = new_head
            self.length -= 1
            return None

        temp = self.head.next
        prev = self.head

        for i in range(1, position - 1):
            temp = temp.next
            prev = prev.next

        if temp.next is None:
            temp.prev.next = None
            temp.prev = None
            self.length -= 1
            return None

        prev.next = temp.next
        temp.next.prev = prev
        temp.next = None
        temp.prev = None
        self.length -= 1

    # Function to print all the Nodes in the Doubly Linked List
    def print_node(self):
        if self.head is None:
            print('Doubly Linked List is Empty!')
        else:
            temp = self.head
            while temp is not None:
                if temp.next is not None:
                    print(temp.data, end='==')
                else:
                    print(temp.data)
                temp = temp.next

    # Function to print the Length of the Doubly Linked List
    def show_length(self):
        print(self.length)


'''
We can initialize the DoublyLinkedList class i.e DoublyLinkedList()
After initializing the LinkedList class we need to create a Node
and assign it to the head of the DoublyLinkedList i.e DoublyLinkedList.head = Node(1)
We can use methods in LinkedList class to manipulate the DoublyLinkedList
'''

# Doubly Linked List Questions

# Question 1
'''
You have a browser of one tab where you start on the homepage and you can visit another url, 
get back in the history number of steps or move forward in the history number of steps.
Input: ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"] - function call
       [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]] - function output
Output : [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
'''


class Tabs:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage):

        # Initializing the homepage and var to keep track of current page

        self.homepage = homepage
        self.home_page = Tabs(self.homepage)
        self.current_page = self.home_page

    def visit(self, url: str) -> None:

        curr_page = self.current_page

        # Checking if page exists after current page
        # If exist we need to remove its pointers
        if curr_page.next:
            curr_page.next = None

        # Updating current page
        self.current_page = curr_page

        # Creating new page and updating current page
        new_page = Tabs(url)
        self.current_page.next = new_page
        new_page.prev = self.current_page
        self.current_page = new_page

    def back(self, steps):

        curr_page = self.current_page

        # Traversing back to the given steps and updating current page
        for i in range(0, steps):
            if curr_page.prev is None:
                curr_page = curr_page
            else:
                curr_page = curr_page.prev

        self.current_page = curr_page

        # Returning data if current page exist
        if self.current_page:
            return self.current_page.data
        else:
            return None

    def forward(self, steps):

        curr_page = self.current_page

        # Traversing forward to the given steps and updating current page
        for i in range(0, steps):
            if curr_page.next is None:
                curr_page = curr_page
            else:
                curr_page = curr_page.next

        self.current_page = curr_page

        # Returning data if current page exist
        if self.current_page:
            return self.current_page.data
        else:
            return None
