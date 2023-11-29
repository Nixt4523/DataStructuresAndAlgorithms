# Stack
"""
Stack is a Linear Data Structure
It follows Last in First out Order LIFO
Insertion and Removal of the Elements is only done on one end
Stacks can be implemented using Arrays or Linked List
"""

'''
Time complexities of Stack Functions
Lookup Function : O(n)
Pop Function : O(1)
Push Function : O(1)
Peek Function : O(1)
'''


# Implementing Stacks using Linked List
# First we need to create Node class to store Data and address of the next Node
class Node:
    # Initializing the Node
    def __init__(self, data):
        self.data = data
        self.next = None


# After creating Node class we need to create Stack class
class Stack:
    # Initializing the Stack
    def __init__(self):
        self.top_node = None
        self.bottom_node = None
        self.length = 0

    # Function to Peek the Top element
    def peek_stack(self):
        if self.top_node is not None:
            print(self.top_node.data)
        else:
            print('Stack is Empty!')

    # Function to Add new Node in the Stack
    def push_node(self, data):
        new_node = Node(data)

        if self.length == 0:
            self.top_node = new_node
            self.bottom_node = new_node
        else:
            ref_pointer = self.top_node
            self.top_node = new_node
            self.top_node.next = ref_pointer

        self.length += 1

    # Function to remove Node from Stack
    def pop_node(self):

        if self.top_node == self.bottom_node:
            self.bottom_node = None

        if self.top_node is None:
            print('Stack is Empty!')
        else:
            top_node = self.top_node
            self.top_node = top_node.next
            self.length -= 1

    # Function to print Stack
    def print_stack(self):
        curr_node = self.top_node

        if self.top_node is None:
            print('Stack is Empty!')

        while curr_node is not None:
            if curr_node.next is not None:
                print(curr_node.data, end='<-')
            else:
                print(curr_node.data)
            curr_node = curr_node.next


'''
We can initialize the Stack class i.e Stack()
After initializing the Stack class we need to create Nodes
to push them into the Stack
We can use methods in Stack class to manipulate the Stack
'''

# Implementing Stack using Arrays
class ArrayStack:

    def __init__(self):
        self.array = []

    def peek_stack(self):
        return self.array[len(self.array) - 1]

    def push_node(self, data):
        self.array.append(data)

    def pop_node(self):
        self.array.pop()

    def print_stack(self):
        print(self.array)


'''
Same as previous we can initialize the ArrayStack class i.e ArrayStack()
Using arrays while implementing Stacks we do not need extra Node class
Its easy to implement
We can use methods in ArrayStack class to manipulate the ArrayStack
'''

# Stack Question

# Question 1
'''
You have to keep track of the base ball game,
using certain rules in a record i.e stack
You're given a list of string operations, where operations[i] is 
the ith operation you must apply to the record with respect to the rules
Rules : # An integer x
          Record a new score of x
        # '+'
          Record a new score that is the sum of the previous two scores
        # 'D'
          Record a new score that is the double of the previous score
        # 'C'
          Invalidate the previous score, removing it from the record
You have to return the sum of the scores in the record
Input: ops = ["5","2","C","D","+"]
Output: 30
Link : https://leetcode.com/problems/baseball-game/
'''


class ScoreStack:

    # Initializing Stack using arrays
    def __init__(self):
        self.array = []

    # Adding push node function to perform given operations
    def push_node(self, data):
        if data == 'C':
            self.array.pop()
        elif data == 'D':
            last_element = self.array[-1]
            self.array.append(last_element * 2)
        elif data == '+':
            self.array.append(self.array[-1] + self.array[-2])
        else:
            self.array.append(int(data))

    # Returning array for calculating final answer
    def get_array(self):

        return self.array


def cal_points(operations):

    ans = 0

    # Creating object of the Stack class
    stack = ScoreStack()

    # Pushing given array's elements to the stack
    for i in range(0, len(operations)):
        stack.push_node(operations[i])

    # Retrieving array from stack
    stack_array = stack.get_array()

    # Calculating sum
    for i in range(0, len(stack_array)):
        ans += stack_array[i]

    # Returning ans
    return ans