#########################################
# MSCS 532 Assignment 2
# Author: Gregory Renteria
# Quick Sort implementation.
#########################################

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

arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)