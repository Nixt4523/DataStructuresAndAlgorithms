# Queues
"""
Queue is a Linear Data Structure
It follows First in First out Order FIFO
Insertion is done at the back of Queue i.e called Enqueue
Deletion is done at the front of Queue i.e called Dequeue
"""

'''
Time complexities of Queue Functions
Lookup Function : O(n)
Peek Function : O(1)
Enqueue Function : O(1)
Dequeue Function : O(1)
'''


# Implementing Queue in Python
# First we need to create Node class to store data and the address of next element in Queue
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# After creating Node class we need to create Queue class
class Queue:

    def __init__(self):
        self.first_element = None
        self.last_element = None
        self.length = 0

    def peek_queue(self):
        first_node = self.first_element.data
        print(f'Peek Node : {first_node}')

    def enqueue(self, data):

        first_node = self.first_element
        last_node = self.last_element

        new_node = Node(data)

        if first_node is None:
            first_node = new_node
            self.first_element = first_node
            self.last_element = first_node
        else:
            last_node.next = new_node
            last_node = last_node.next
            self.last_element = last_node

        self.length += 1

    def dequeue(self):

        first_node = self.first_element
        next_node = first_node.next

        if first_node is None:
            print('Queue is Empty!')

        first_node = next_node
        self.first_element = first_node
        self.length -= 1

    def print_queue(self):

        curr_node = self.first_element

        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next


'''
We can initialize the Queue class i.e Stack()
We can use methods in Queue class to manipulate the Queue
'''

# Graph Questions

# Question 1
'''
You're given Arrays students standing in a Queue and sandwiches
if student at the front of the Queue is equal to the sandwich at 0th position in sandwich array
then student takes the sandwich and leaves the Queue
if not then student leaves the Queue and goes to the back of the Queue
return the number of students that are unable to eat sandwich
Input: students = [1, 1, 0, 0]
       sandwiches = [0, 1, 0, 1]
Output : 0
Link : https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
'''
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]

while students and sandwiches and sandwiches[0] in students:

    if students[0] == sandwiches[0]:
        students.pop(0)
        sandwiches.pop(0)

    else:
        temp = students.pop(0)
        students.append(temp)

print(len(students))  # Returning ans
