#!/usr/bin/python3

'''
Name: Kevin Harvell
Date: 1/9/19
About: This program has a function called mergeSort that recursively splits
an array in half until 1 element in each array. Then builds sorted arrays
by combining the smaller arrays and comparing the values.
It takes an input file and sorts using the insertionSort function, and creates
an output file.

# The following code is based on pseudocode from Introduction to Algorithms - 3rd Edition p.26
'''

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


readFile = open("data.txt")
lines = readFile.read().splitlines()
readFile.close()

insertFile = open("insert.txt", "w+")

for line in lines:
    # Turn each line into an array
    tempArr = line.split(" ")
    tempArr.pop(0)
    # Convert string array into ints
    numArr = [int(num) for num in tempArr]
    # Sort the array of ints
    sortedArr = insertionSort(numArr)
    # Convert array back into strings
    strArr = [str(num) for num in sortedArr]
    outputLine = ' '.join(strArr)
    print(outputLine)
    insertFile.write(outputLine + '\n')

insertFile.close()



