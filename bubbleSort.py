import copy

def bubbleSort (inputList):
    sortedList = copy.deepcopy(inputList)
    listSize = len(inputList)
    while listSize > 1:
        for i in range(listSize-1):
            if(sortedList[i] > sortedList[i+1]):
                buffer = sortedList[i]
                sortedList[i] = sortedList[i+1]
                sortedList[i+1] = buffer
        listSize -= 1
    return sortedList