# Arrays in Python

"""
An Array is a Linear Data Structure
It requires contiguous memory location
Arrays are called Lists in Python
Arrays are Dynamic in Python
Elements can be accessed by their Indexes
In Python Arrays can contain different types of variables
"""

array = ['a', 'b', 'c', 'd']
'''
Memory allocation of Array
4*4 = In 32 bit Computers each element in an Array 
      get 4 bytes of Memory      
      So in 32 bit Computers an Array with 4 elements will
      get 16 bytes of Memory allocation
4*8 = In 64 bit Computers each element in an Array
      get 8 bytes of Memory
      So in 64 bits Computers an Array with 4 elements will 
      get 32 bytes of Memory allocation
'''

# Array Functions in Python

# Accessing element from Array
index_2 = array[1]
'''
Gets the element from an Array at the index 1 i.e 'b'
The time complexity of this Function is O(1) i.e Constant Time
'''

# Append Function
array.append('e')
'''
Adds 'e' to the end of the Array
The new Array will be ['a', 'b', 'c', 'd', 'e']
The time complexity of this Function is O(1) i.e Constant Time 
'''

# Pop Function
array.pop()
'''
Removes the last element in the Array
The new Array will be ['a', 'b', 'c', 'd']
The time complexity of this Function is O(1) i.e Constant Time
'''

# Inserting at the Beginning of the Array
array.insert(0, 'x')
'''
Inserts the given element in the Beginning of the Array 
The new Array will be ['x', 'a', 'b', 'c', 'd']
The time complexity of this Function is O(n) i.e Linear Time
'''

# Inserting at Specific Index in an Array
array.insert(1, 'y')
'''
Inserts the given element at the given index in the Array
The new Array will be ['x', 'y', 'a', 'b', 'c', 'd']
The time complexity of this Function is O(n) i.e Linear Time
'''


# Implementation of the Array in Python
class Array:
    # Initializing the array
    def __init__(self):
        self.array = []

    # Method to access the element
    def get(self, element):
        return self.array[element]

    # Method to add the given element at the end of an Array
    def push(self, element):
        self.array.append(element)

    # Method to delete last element of an Array
    def pop(self):
        self.array.pop()

    # Method to insert the given element at the start of an Array
    def insert_beginning(self, element):
        self.array.insert(0, element)

    # Method to inset the given element at the given index of an Array
    def insert_specific(self, index, element):
        self.array.insert(index, element)


'''
We can initialize the Array class i.e Array()
We can use the methods in the Array class to Manipulate the Array
'''

# Array Questions

# Question 1
'''
Create a Function to reverse the String
Input : "Hi my name is Nikhil" 
Output : "lihkiN si eman ym iH"
'''


def reverse_string(input_string):
    temp_string = ''
    for i in input_string:
        temp_string = i + temp_string

    print(temp_string)
    return temp_string


'''
Calling the reverse_string() and passing the input_string
to it will reverse the string and will print it
'''

# Question 2
'''
Create a Function that will merge two sorted arrays together
Input : [0, 3, 4, 31], [4, 6, 30]
Output : [0 , 3 , 4 , 4 , 6 , 30 , 31]
'''


def merge_sorted_arrays(array1, array2):
    array1_size = len(array1)
    array2_size = len(array2)

    temp_array = []
    i = 0
    j = 0

    while i < array1_size and j < array2_size:
        if array1[i] < array2[j]:
            temp_array.append(array1[i])
            i += 1
        else:
            temp_array.append(array2[j])
            j += 1

    merged_array = temp_array + array1[i:] + array2[j:]
    print(merged_array)
