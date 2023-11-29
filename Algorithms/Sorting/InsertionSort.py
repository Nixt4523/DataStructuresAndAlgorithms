# Insertion Sort
"""
Insertion Sort is very useful when you know if array is almost sorted
We can get O(n) Time complexity if the array is almost sorted
"""

'''
Time complexities of Insertion Sort
Best Case : O(n)
Average Case : O(n^2)
Worst Case : O(n^2)
'''

'''
Space complexity of Insertion Sort
Worst Case : O(n)
'''

# Implementing Insertion Sort in Python

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 238, 4, 0]


def insertion_sort(array):

    length = len(array)

    for i in range(1, length):

        key = array[i]

        j = i - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

    print(array)


insertion_sort(numbers)
