# Quick Sort
"""
Quick Sort is similar to Merge Sort both of them uses Divide and Conquer technique
Quick Sort uses pivoting technique to divide array into the sub array until they are sorted
Quick Sort is better than Merge Sort in terms of space complexity
But Merge Sort is better in Worst Time Complexity than Quick Sort
"""

'''
Time complexities of Quick Sort
Best Case : O(n log(n))
Average Case : O(n log(n))
Worst Case : O(n^2)
'''

'''
Space complexity of Quick Sort
Worst Case : O(log(n))
'''

# Implementing Quick Sort in Python

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 238, 4, 0]

'''
This implementation of Quick Sort utilizes pivot as the last element in an Array
It has pointer to keep track of the elements smaller than pivot 
At the end of the partition() function, the pointer is swapped with pivot
to come up with a sorted Array relative to the pivot
'''


def partition(array, low, high):

    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]

    return i + 1


def quick_sort(array, low, high):

    if low < high:

        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


quick_sort(numbers, 0, len(numbers) - 1)
