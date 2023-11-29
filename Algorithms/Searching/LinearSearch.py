# Linear Search
"""
Linear Search is defined as Sequential Search
Which starts at one end and goes through each element of array until the desired element is found
"""

'''
Time complexity of Linear Search
Average Case : O(n)
'''

'''
Space complexity of Linear Search
Average Case : O(n)
'''

# Implementing Linear Search in Python

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 238, 4, 0]
find = 1


def linear_search(array, target):
    for i in range(0, len(array)):

        if array[i] == target:
            print(f'Target Found at index : {i}')
            return i


linear_search(numbers, find)
