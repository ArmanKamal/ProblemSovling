from array import array
from turtle import right

## Solution 1 ##

def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        firstNumber = array[i]
        for j in range(i+1, len(array)):
            secondNumber = array[j]
            if firstNumber+ secondNumber == targetSum:
                return [firstNumber, secondNumber]
    return []


array = [3, 5, -4, 8 , 11, 1, -1 ,6]
targetSum = 10

print(twoNumberSum(array,targetSum))


## Solution 2 ##
## Time Complexity O(n) ## Space Complexity O(n)

def twoNumberSumSol2(array, targetSum):
    targetDictonary = {}
    for i in range(len(array)):
        if targetSum-array[i] in targetDictonary:
            return [targetSum-array[i], array[i]]
        else:
            targetDictonary[array[i]] = True
    return []


## Solution 3 ##
##  ##

def twoNumberSumSol2(array, targetSum):
    sorted_array = array.sort()
    left_pointer = 0
    right_pointer = len(array)-1

    for i in range(len(sorted_array)):
        if sorted_array[i]+sorted_array[i+1] > targetSum:
            left_pointer = left_pointer+1
