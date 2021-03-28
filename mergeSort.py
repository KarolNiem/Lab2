def mergeSort(inputList):
    if len(inputList) > 1:
        middle = len(inputList) // 2
        leftList = inputList[:middle]
        rightList = inputList[middle:]
        mergeSort(leftList)
        mergeSort(rightList)
        i, j, k = 0, 0, 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                inputList[k] = leftList[i]
                i += 1
                k += 1
            else:
                inputList[k] = rightList[j]
                j += 1
                k += 1
        while i < len(leftList):
            inputList[k] = leftList[i]
            i += 1
            k += 1
        while j < len(rightList):
            inputList[k] = rightList[j]
            j += 1
            k += 1

