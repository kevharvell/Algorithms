#!/usr/bin/python3

'''
Name: Kevin Harvell
Date: 1/17/19
About: This program has a function called mergeSort that recursively splits
an array in quarters until 1 element in each array. Then builds sorted arrays
by combining the smaller arrays and comparing the values.
It takes an input file and sorts using the mergeSort function, and creates
an output file.

# The following code is based on code from
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
'''

import random
import time

def mergeSort(arr):
    # If array is greater than 1, sort. Otherwise, no need to sort
    if len(arr) > 1:
        # Split the array into 4 quarters
        mid = len(arr) // 2
        q1mid = mid // 2
        q3mid = mid + q1mid
        q1 = arr[:q1mid]
        q2 = arr[q1mid:mid]
        q3 = arr[mid:q3mid]
        q4 = arr[q3mid:]
        left = []
        right = []

        # Keep splitting arrays into quarters until only one or less element
        # in each quarter
        mergeSort(q1)
        mergeSort(q2)
        mergeSort(q3)
        mergeSort(q4)

        i = 0
        j = 0
        k = 0
        # If there are elements not yet compared in the first two quarters,
        # compare and put lower/equal value in next spot in left array
        while i < len(q1) and j < len(q2):
            if q1[i] < q2[j]:
                left.append(q1[i])
                i = i + 1
            else:
                left.append(q2[j])
                j = j + 1
            k = k + 1
        # There are still elements in the q1 array
        # Put them in the next spot in left array
        while i < len(q1):
            left.append(q1[i])
            i = i + 1
            k = k + 1
        # There are still elements in the q2 array
        # Put them in the next spot in left array
        while j < len(q2):
            left.append(q2[j])
            j = j + 1
            k = k + 1

        i = 0
        j = 0
        k = 0
        # If there are elements not yet compared in the last two quarters,
        # compare and put lower/equal value in next spot in right array
        while i < len(q3) and j < len(q4):
            if q3[i] < q4[j]:
                right.append(q3[i])
                i = i + 1
            else:
                right.append(q4[j])
                j = j + 1
            k = k + 1
        # There are still elements in the q3 array
        # Put them in the next spot in right array
        while i < len(q3):
            right.append(q3[i])
            i = i + 1
            k = k + 1
        # There are still elements in the q4 array
        # Put them in the next spot in right array
        while j < len(q4):
            right.append(q4[j])
            j = j + 1
            k = k + 1

        i = 0
        j = 0
        k = 0
        # If there are elements not yet compared in both halves, compare and
        # put lower/equal value in next spot in array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
            k = k + 1
        # There are still elements in the left array
        # Put them in the next spot in array
        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1
        # There are still elements in the right array
        # Put them in the next spot in array
        while j < len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1
    return arr


unsorted = []
n = int(input("Enter the number of elements in the array: "))
for x in range(n):
    unsorted.append(random.randint(0, 10000))
print(unsorted)
t0 = time.time()
print(mergeSort(unsorted))
t1 = time.time()
print(t1 - t0)