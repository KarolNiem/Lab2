from quickSort import quickSort
from mergeSort import mergeSort
from Lab2.countingSort import countingSort
from Lab2.listToString import listToString
from test import test
import matplotlib.pyplot as plt
import timeit
import sys
import copy

filename = sys.argv[1]
file = open(filename, "r").read()
bubbleLorem = open("../bubbleLorem.txt", "w")
quickLorem = open("../quickLorem.txt", "w")
mergeLorem = open("../mergeLorem.txt", "w")
countingLorem = open("../countingLorem.txt", "w")

text = file.replace('\n', '')
text = [char for char in text]

bubbleSortTime = []
quickSortTime = []
mergeSortTime = []
countingSortTime = []
elements = []

setupOptions = '''
from bubbleSort import bubbleSort
from quickSort import quickSort
from mergeSort import mergeSort
from countingSort import countingSort
file = open("lorem_ipsum.txt", "r").read()
text = [char for char in file]'''

for i in range(1, 1000, 100):
    elements.append(i)
    bubbleSortTime.append(timeit.timeit("bubbleSort(text[:{}])".format(i), setup=setupOptions, number=5))
    quickSortTime.append(timeit.timeit("quickSort(text[:{}])".format(i), setup=setupOptions, number=5))
    mergeSortTime.append(timeit.timeit("mergeSort(text[:{}])".format(i), setup=setupOptions, number=5))
    countingSortTime.append(timeit.timeit("countingSort([ord(x) for x in text[:{}]],255)".format(i), setup=setupOptions, number=5))

# bubble = bubbleSort(text)
# bubbleLorem.write(listToString(bubble))
quick = quickSort(text)
quickLorem.write(listToString(quick))
merge = copy.deepcopy(text)
mergeSort(merge)
mergeLorem.write(listToString(merge))
counting = countingSort([ord(x) for x in text], 255)
countingLorem.write(listToString([chr(x) for x in counting]))

fig = plt.figure()
plt.plot(elements, bubbleSortTime, label='Bubble sort', color='red')
plt.plot(elements, quickSortTime, label='Quick sort', color='blue')
plt.plot(elements, mergeSortTime, label='Merge sort', color='green')
plt.plot(elements, countingSortTime, label='Counting sort', color='orange')
plt.xlabel('Number of elements [n]')
plt.ylabel('Time [inputList]')
plt.title("Sorting algorithms comparison graphs")
plt.legend()
plt.show()
fig.savefig("Graphs.png", dpi=fig.dpi)
bubbleLorem.close()
quickLorem.close()
mergeLorem.close()
countingLorem.close()
test(30)
