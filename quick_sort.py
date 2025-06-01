#########################################
# MSCS 532 Assignment 2
# Author: Gregory Renteria
# Quick Sort implementation.
#########################################

def quick_sort(arr):
    if len(arr) <= 1:
        return arr