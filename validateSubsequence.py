## Time O(n) & Space O(1) ##

def isValidSubsequence(array, sequence):
    sequenceIndex = 0
    # Write your code here.
    for num in array:
        if sequenceIndex == len(sequence):
            break
        if sequence[sequenceIndex] == num:
            sequenceIndex+=1
        
    return sequenceIndex == len(sequence)


## With while loop ##


def isValidSubsequenceWith(array, sequence):
    sequenceIndex = 0
    arrayIndex = 0

    while arrayIndex<len(array) and sequenceIndex<len(sequence):
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex+=1
        arrayIndex += 1

    return sequenceIndex == len(sequence)
