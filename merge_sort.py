#########################################
# MSCS 532 Assignment 2
# Author: Gregory Renteria
# Merge Sort implementation.
#########################################

import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Compare elements from left and right and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add remaining elements (if any)
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

# Example for sorted data
sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Sorted Input:", sorted_data)
print("Output:", merge_sort(sorted_data), "\n")

# Example for reverse sorted data
reverse_sorted_data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Reverse Sorted Input:", reverse_sorted_data)
print("Output:", merge_sort(reverse_sorted_data), "\n")

# Example for random data
random_data = random.sample(range(1, 100), 10)
print("Random Input:", random_data)
print("Output:", merge_sort(random_data))