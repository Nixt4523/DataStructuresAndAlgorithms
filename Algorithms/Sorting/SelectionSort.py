# Selection Sort
"""
Selection Sort scans through the array and finds the smallest element in the array
After finding the smallest element we swap it to the right index and continue the process
"""

'''
Time complexities of Selection Sort
Best Case : O(n^2)
Average Case : O(n^2)
Worst Case : O(n^2)
'''

'''
Space complexity of Selection Sort
Worst Case : O(1)
'''

# Implementing Selection Sort in Python

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 238, 4, 0]


def selection_sort(array):

    length = len(array)

    for i in range(0, length):

        # Setting current index as minimum index
        min_index = i

        for j in range(i + 1, length):
            if array[j] < array[min_index]:

                '''
                Updating the minimum index if current index
                is lower than what we had previously
                '''
                min_index = j

        # Swapping elements
        array[i], array[min_index] = array[min_index], array[i]

    print(array)


selection_sort(numbers)
