def quickSort(inputList):
    lowerList = []
    pivotList = []
    greaterList = []
    listSize = len(inputList)

    if listSize > 1:
        pivot = inputList[listSize-1]
        for x in inputList:
            if x < pivot:
                lowerList.append(x)
            elif x == pivot:
                pivotList.append(x)
            elif x > pivot:
                greaterList.append(x)
        return quickSort(lowerList) + pivotList + quickSort(greaterList)
    else:
        return inputList