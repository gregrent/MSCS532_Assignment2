#########################################
# MSCS 532 Assignment 2
# Author: Gregory Renteria
# Quick Sort implementation.
#########################################

import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot element (here we choose the middle element)
    pivot = arr[len(arr) // 2]

    # Partition the array into three sub-arrays:
    # - elements less than pivot
    # - elements equal to pivot
    # - elements greater than pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right sub-arrays,
    # then combine them with the middle part
    return quick_sort(left) + middle + quick_sort(right)


# Example for sorted data
sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Sorted Input:", sorted_data)
print("Output:", quick_sort(sorted_data), "\n")

# Example for reverse sorted data
reverse_sorted_data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Reverse Sorted Input:", reverse_sorted_data)
print("Output:", quick_sort(reverse_sorted_data), "\n")

# Example for random data
random_data = random.sample(range(1, 100), 10)
print("Random Input:", random_data)
print("Output:", quick_sort(random_data))