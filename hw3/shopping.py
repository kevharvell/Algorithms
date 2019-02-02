#!/usr/bin/python3

'''
Name: Kevin Harvell
Date: 1/26/19
About: This program has a function called knapsack that creates a 2D array representing
weight and items to keep track of the maximum benefit in the knapsack. It first initializes
a row and column to 0 to represent no items and no weight, or in other words, an empty knapsack.
Then, it loops through from weight 1 to max weight to see what can be stored in the knapsack
to produce the maximum benefit.

# This code was taken/modified from OSU 325 lecture slides regarding Knapsack 0-1 AND
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
'''

def knapSack(items, maxWeight):
    K = [[0 for x in range(maxWeight + 1)] for x in range(len(items) + 1)]

    # Build table K[][] in bottom up manner
    for i in range(len(items) + 1):
        for w in range(maxWeight + 1):
            # Zero out first row and column
            if i == 0 or w == 0:
                K[i][w] = 0
            # If item weight is less than iteration weight
            elif int(items[i - 1][1]) <= w:
                K[i][w] = max(int(items[i - 1][0]) + K[i - 1][w - int(items[i - 1][1])], K[i - 1][w])
            # Take previous row best weight
            else:
                K[i][w] = K[i - 1][w]
    # Get the sequence of items
    pickedItems = []
    i = len(items)
    w = maxWeight
    while i > 0 and w > 0:
        # If this item is the same as the row above, move on
        if K[i][w] == K[i - 1][w]:
            i -= 1
        # Else, this is an item, move into pickedItems
        else:
            pickedItems.insert(0, i)
            i -= 1
            w -= int(items[i - 1][1])
    results = [K[len(items)][maxWeight], pickedItems]
    return results


readFile = open("shopping.txt")
lines = readFile.read().splitlines()
readFile.close()

resultsFile = open("results.txt", "w+")
outputLines = ""

lineNum = 0
testCases = int(lines[lineNum])
lineNum += 1


for T in range(testCases):
    numItems = int(lines[lineNum])
    lineNum += 1
    items = []
    for i in range(numItems):
        items.append(lines[lineNum].split())
        lineNum += 1
    numFam = int(lines[lineNum])
    lineNum += 1
    maxWeights = []
    for f in range(numFam):
        maxWeights.append(int(lines[lineNum]))
        lineNum += 1
    outputLines += "Test Case " + repr(T + 1) + "\n"
    totalWeight = 0
    memberItems = []
    for W in range(0, len(maxWeights)):
        results = knapSack(items, maxWeights[W])
        weight = results[0]
        totalWeight += weight
        memberItems.append(results[1])
    outputLines += "Total Price " + repr(totalWeight) + "\n"
    outputLines += "Member Items " + "\n"
    for W in range(0, len(maxWeights)):
        outputLines += "\t" + repr(W + 1) + ": "
        for item in range(0, len(memberItems[W])):
            outputLines += repr(memberItems[W][item]) + " "
        outputLines += "\n"
print(outputLines)

outputLines = outputLines.rstrip('\n')
resultsFile.write(outputLines)

resultsFile.close()