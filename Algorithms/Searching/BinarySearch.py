# Binary Search

"""
Binary Search uses a technique Divide and Conquer
An array must be sorted to use Binary Search
"""

'''
Time complexity of Binary Search
Average Case : O(log(n))
'''

'''
Space complexity of Binary Search
Average Case : O(1)
'''

# Implementing Binary Search in Python

numbers = [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 238]
find = 99


def binary_search_iterative(array, target):

    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:

        mid_index = (left_index + right_index) // 2
        mid_number = array[mid_index]

        if mid_number == target:
            print(f'Target Found at : {mid_index}')
            return mid_index

        if mid_number < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    print('Target does not exist')
    return -1


binary_search_iterative(numbers, find)
