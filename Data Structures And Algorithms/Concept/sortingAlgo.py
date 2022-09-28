lst = [1, 23, 3, 55, 90, 45, 11]

# normal sorting
#sorted_list = []
# for i in range(len(lst)):
#     sorted_list.append(min(lst))
#     lst.remove(min(lst))
# print(sorted_list)

# Selection Sort


def selectionSort(arr):
    for i in range(len(arr)):
        lo = i
        for j in range(i+1, len(lst)):
            if arr[lo] > arr[j]:
                lo = j
        arr[i], arr[lo] = arr[lo], arr[i]

    return arr


print(selectionSort(lst))
# print(lst)
