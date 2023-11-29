# Bubble Sort
"""
Bubble Sort comes from the idea of Bubbling Up
In Bubble Sort we need to Bubble Up the largest number
and continue the process to find next largest number one by one
Bubble Sort is easy to implement, but it is not very Efficient
"""

'''
Time complexities of Bubble Sort
Best Case : O(n)
Average Case : O(n^2)
Worst Case : O(n^2)
'''

'''
Space complexity of Bubble Sort
Worst Case : O(1)
'''

# Implementing Bubble Sort in Python
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 238, 4, 0]


def bubble_sort(array):
    length = len(array)

    for i in range(0, length):
        for j in range(0, length - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print(array)


bubble_sort(numbers)
