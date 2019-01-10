#!/usr/bin/python3

'''
Name: Kevin Harvell
Date: 1/9/19
About: This program has a function called mergeSort that recursively splits
an array in half until 1 element in each array. Then builds sorted arrays
by combining the smaller arrays and comparing the values.
It takes an input file and sorts using the mergeSort function, and creates
an output file.

# The following code is based on code from
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
'''

def mergeSort(arr):
    # If array is greater than 1, sort. Otherwise, no need to sort
    if len(arr) > 1:
        # Split the array into 2 halves
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # Keep splitting arrays into halves until only one element in both halves
        mergeSort(left)
        mergeSort(right)

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


readFile = open("data.txt")
lines = readFile.read().splitlines()
readFile.close()

mergeFile = open("merge.txt", "w+")

for line in lines:
    # Turn each line into an array
    tempArr = line.split(" ")
    tempArr.pop(0)
    # Convert string array into ints
    numArr = [int(num) for num in tempArr]
    # Sort the array of ints
    sortedArr = mergeSort(numArr)
    # Convert array back into strings
    strArr = [str(num) for num in sortedArr]
    outputLine = ' '.join(strArr)
    print(outputLine)
    mergeFile.write(outputLine + '\n')

mergeFile.close()