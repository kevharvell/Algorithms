#!/usr/bin/python3

'''
Name: Kevin Harvell
Date: 1/9/19
About: This program has a function called mergeSort that recursively splits
an array in half until 1 element in each array. Then builds sorted arrays
by combining the smaller arrays and comparing the values.
It takes an input file and sorts using the insertionSort function, and creates
an output file.
It creates an array of random numbers between 1 and 10000 of size n and
times how long it takes to sort the array

# The following code is based on pseudocode from Introduction to Algorithms - 3rd Edition p.26
'''

import random
import time

def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        # Insert arr[j] into the sorted sequence
        i = j
        while i > 0 and arr[i - 1] > key:
            arr[i] = arr[i - 1]
            i = i - 1
        arr[i] = key
    return arr


unsorted = []
n = int(input("Enter the number of elements in the array: "))
for x in range(n):
    unsorted.append(random.randint(0, 10000))
print(unsorted)
t0 = time.time()
print(insertionSort(unsorted))
t1 = time.time()
print(t1 - t0)



