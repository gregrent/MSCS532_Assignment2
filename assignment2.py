#############################################
# MSCS 532 Assignment 2
# Author: Gregory Renteria
# Merge Sort and Quick Sort implementations.
#############################################

import random
import time
import tracemalloc

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

# Example for merge sort sorted data
sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Merge Sort Sorted Input:", sorted_data)
print("Output:", merge_sort(sorted_data), "\n")

# Example for merge sort reverse sorted data
reverse_sorted_data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Merge Sort Reverse Sorted Input:", reverse_sorted_data)
print("Output:", merge_sort(reverse_sorted_data), "\n")

# Example for merge sort random data
random_data = random.sample(range(1, 100), 10)
print("Merge Sort Random Input:", random_data)
print("Output:", merge_sort(random_data), "\n")

# Example for quick sort sorted data
sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Quick Sort Sorted Input:", sorted_data)
print("Output:", quick_sort(sorted_data), "\n")

# Example for quick sort reverse sorted data
reverse_sorted_data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Quick Sort Reverse Sorted Input:", reverse_sorted_data)
print("Output:", quick_sort(reverse_sorted_data), "\n")

# Example for quick sort random data
random_data = random.sample(range(1, 100), 10)
print("Quick Sort Random Input:", random_data)
print("Output:", quick_sort(random_data), "\n")

# Performance metrics for merge sort
tracemalloc.start()
start = time.perf_counter()
merge_sort(random_data.copy())
end = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"[Merge Sort] Time: {end - start:.6f}s, Peak Memory: {peak / 1024:.2f} KB", "\n")

# Performance metrics for quick sort
tracemalloc.start()
start = time.perf_counter()
quick_sort(random_data.copy())
end = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"[Quick Sort] Time: {end - start:.6f}s, Peak Memory: {peak / 1024:.2f} KB")