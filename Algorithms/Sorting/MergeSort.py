# Merge Sort
"""
Merge Sort uses Divide and Conquer technique
"""

'''
Time complexities of Merge Sort
Best Case : O(n log(n))
Average Case : O(n log(n))
Worst Case : O(n log(n))
'''

'''
Space complexity of Merge Sort
Worst Case : O(n)
'''

# Implementing Merge Sort in Python

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 238, 4, 0]


def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted_arrays(left, right)


def merge_sorted_arrays(array1, array2):
    sorted_array = []

    len_array1 = len(array1)
    len_array2 = len(array2)

    i = 0
    j = 0

    while i < len_array1 and j < len_array2:

        if array1[i] <= array2[j]:
            sorted_array.append(array1[i])
            i += 1
        else:
            sorted_array.append(array2[j])
            j += 1

    while i < len_array1:
        sorted_array.append(array1[i])
        i += 1

    while j < len_array2:
        sorted_array.append(array2[j])
        j += 1

    return sorted_array


print(merge_sort(numbers))
