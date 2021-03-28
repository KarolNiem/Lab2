from Lab2.bubbleSort import bubbleSort
from Lab2.quickSort import quickSort
from Lab2.mergeSort import mergeSort
from Lab2.countingSort import countingSort
import copy
import random

def test(number):
    randomList = []
    for i in range(0, number):
        n = random.randint(1, number)
        randomList.append(n)
    merge = copy.deepcopy(randomList)
    mergeSort(merge)
    counting = copy.deepcopy(randomList)
    print("\nWynik sortowania metoda sortowania babelkowego:\n", bubbleSort(randomList))
    print("\nWynik sortowania metoda sortowania szybkiego:\n", quickSort(randomList))
    print("\nWynik sortowania metoda sortowania przez zliczanie:\n", countingSort(counting, number))
    print("\nWynik sortowania metoda sortowania przez scalanie:\n", merge)
    print("\nOryginalna tablica wynosi:\n", randomList)
