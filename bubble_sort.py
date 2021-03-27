import copy
def bubble_sort(list):
    sortedList = copy.deepcopy(list)
    listSize = len(list)
    while listSize > 1:
        for j in range(listSize-1):
            if(sortedList[j] > sortedList[j+1]):
                buffer = sortedList[j]
                sortedList[j] = sortedList[j+1]
                sortedList[j+1] = buffer
        listSize -= 1
    return sortedList