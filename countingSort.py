def countingSort(inputList, maximum):
    numberList = [0] * (maximum + 1)
    outputList = []
    for i in inputList:
        numberList[i] += 1
    for i in range(maximum + 1):
        for j in range(numberList[i]):
            outputList.append(i)
    return outputList