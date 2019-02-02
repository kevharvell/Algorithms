#!/usr/bin/python3

'''
Name: Kevin Harvell
Date: 2/2/19
About: This program has uses a greedy algorithm to select compatible activities
from the latest start time to the earliest.

# The following code is based on code from
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
'''

ACTIVITY_NUM = 0
START_TIME = 1
FINISH_TIME = 2


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
            if left[i][START_TIME] > right[j][START_TIME]:
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


def activitySelector(activityArr):
    n = len(activityArr)
    # Sort activity list in descending order by start time
    sortedActivityArr = mergeSort(activityArr)
    selectedActivities = []
    # Append first activity to selected activities because it has
    # the latest start time
    selectedActivities.append(sortedActivityArr[0][ACTIVITY_NUM])
    i = 0
    for m in range(1, n):
        # If the next activity has a finish time that is before or equal the current
        # activity's start time, put activity into selected activities
        if sortedActivityArr[m][FINISH_TIME] <= sortedActivityArr[i][START_TIME]:
            selectedActivities.insert(0, activityArr[m][ACTIVITY_NUM])
            i = m
    return selectedActivities


readFile = open("act.txt")
lines = readFile.read().splitlines()
readFile.close()

outputLines = ""
lineNum = 0

setNum = 1

while lineNum < len(lines):
    numActivities = int(lines[lineNum])
    lineNum += 1
    activityArr = []
    for i in range(numActivities):
        tempArr = lines[lineNum].split(' ')
        tempArr = list(map(int, tempArr))
        activityArr.append(tempArr)
        lineNum += 1
    selectedActivities = activitySelector(activityArr)
    print("Set {}").format(setNum)
    print("Number of activities selected = {}").format(len(selectedActivities))
    print("Activities {}").format(" ".join(str(x) for x in selectedActivities))
    print
    setNum += 1

