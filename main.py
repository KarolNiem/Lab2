from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import mergesort
from counting_sort import counting_sort
from listToString import listToString
import matplotlib.pyplot as plt
import numpy as np
import timeit
import sys
import copy

filename = sys.argv[1]
file = open(filename, "r").read()
quick_lorem = open("quick_lorem.txt", "w")
merge_lorem = open("merge_lorem.txt", "w")
counting_lorem = open("counting_lorem.txt", "w")

text = file.replace('\n','')
text = [char for char in text]

bubble_sort_time = []
quick_sort_time = []
merge_sort_time = []
counting_sort_time = []
elements=[]

sor = '''
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import mergesort
from counting_sort import counting_sort
import random
randomlist=[]
for i in range(1,3000):
    l = random.randint(0,3000)
    randomlist.append(l)
n=len(randomlist)'''

for i in range(1,1000,100):
    elements.append(i-1)
    bubble_sort_time.append(timeit.timeit("bubble_sort(randomlist[:{}])".format(i), setup=sor, number=5))
    quick_sort_time.append(timeit.timeit("quick_sort(randomlist[:{}])".format(i), setup=sor, number=5))
    merge_sort_time.append(timeit.timeit("mergesort(randomlist[:{}])".format(i), setup=sor, number=5))
    counting_sort_time.append(timeit.timeit("counting_sort(randomlist[:{}],3000)".format(i), setup=sor, number=5))

#bubble = bubble_sort(randomlist)
quick=quick_sort(text)
quick_lorem.write(listToString(quick))
merge=copy.deepcopy(text)
mergesort(merge)
merge_lorem.write(listToString(merge))
counting=counting_sort([ord(x) for x in text],255)
counting_lorem.write(listToString([chr(x) for x in counting]))

'''print(bubble)
print(quick)
print(merge)
print(counting)
print(tablica)'''

fig=plt.figure()
plt.plot(elements, bubble_sort_time, label='bubble_sort')
plt.plot(elements, quick_sort_time, label='quick_sort')
plt.plot(elements, merge_sort_time, label='merge_sort')
plt.plot(elements, counting_sort_time, label='counting_sort')
plt.xlabel('Number of elements')
plt.ylabel('time[s]')
plt.title("Sorting algorithms comparison graphs")
plt.legend()
plt.show()
fig.savefig("Wykresy.png",dpi=fig.dpi)
quick_lorem.close()
merge_lorem.close()