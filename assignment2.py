#############################################
# MSCS 532 Assignment 2
# Author: Gregory Renteria
# Merge Sort and Quick Sort implementations.
#############################################

import random
import time
import tracemalloc
import matplotlib.pyplot as plt

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

# Measure Merge Sort performance
tracemalloc.start()
start = time.perf_counter()
merge_sort(random_data.copy())
end = time.perf_counter()
current, peak_merge = tracemalloc.get_traced_memory()
tracemalloc.stop()
merge_time = end - start

print(f"[Merge Sort] Time: {merge_time:.6f}s, Peak Memory: {peak_merge / 1024:.2f} KB\n")

# Measure Quick Sort performance
tracemalloc.start()
start = time.perf_counter()
quick_sort(random_data.copy())
end = time.perf_counter()
current, peak_quick = tracemalloc.get_traced_memory()
tracemalloc.stop()
quick_time = end - start

print(f"[Quick Sort] Time: {quick_time:.6f}s, Peak Memory: {peak_quick / 1024:.2f} KB")

# Plotting execution time
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(['Merge Sort', 'Quick Sort'], [merge_time, quick_time], color=['blue', 'orange'])
plt.ylabel('Time (seconds)')
plt.title('Execution Time')

# Plotting peak memory usage
plt.subplot(1, 2, 2)
plt.bar(['Merge Sort', 'Quick Sort'], [peak_merge / 1024, peak_quick / 1024], color=['blue', 'orange'])
plt.ylabel('Memory (KB)')
plt.title('Peak Memory Usage')

plt.tight_layout()
plt.show()