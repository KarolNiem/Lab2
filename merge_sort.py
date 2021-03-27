def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_list = array[:mid]
        right_list = array[mid:]
        mergesort(left_list)
        mergesort(right_list)
        j = 0
        i = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                array[k] = left_list[i]
                i += 1
                k += 1
            else:
                array[k] = right_list[j]
                j += 1
                k += 1
        while i < len(left_list):
            array[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            array[k] = right_list[j]
            j += 1
            k += 1

