## Solution 1 ##

from turtle import right


def sortedSqaureArray(array):
    new_array = [0 for x in array]

    # new_array = [0] * len(array)


    for i in range(len(array)):
        new_array[i] = array[i]* array[i]

    new_array.sort()

    return new_array

print(sortedSqaureArray([1,2,3,5,6,8,9]))


## Solution 2 ##

def sortedSqaureArraySol2(array):
    left = 0
    right = len(array)-1

    new_array = [0] * len(array)

    for i in reversed(range(len(array))):
        if abs(array[left]) > abs(array[right]):
            new_array[i] = array[left] * array[left]
            left+=1
        else:
            new_array[i] = array[right] * array[right]
            right-=1

    return new_array


print(sortedSqaureArraySol2([1,2,3,5,6,8,9]))




