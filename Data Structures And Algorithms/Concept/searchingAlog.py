# linear Search
lst = [1, 3, 22, 34, 45, 66, 77, 90]
x = 1


def linearSearch(arr, x):
    for i in range(len(arr)):
        if x == lst[i]:
            print(f'{x} present at index {i}')
            break
    else:
        print(f'{x} element not present in list')

    # one line
    res = f'{x} is present at index {arr.index(x)}' if x in lst else f'{x} is not in list'
    print(res)


def binarySearch(arr, x):
    l, r = 0, len(arr)-1

    while r-l > 1:
        mid = (l+r)//2
        if x > arr[mid]:
            l = mid+1
        elif x < arr[mid]:
            r = mid-1

    if arr[l] == x:
        return f'{x} found at index {l}'
    elif arr[r] == x:
        return f'{x} found at index {r}'
    else:
        return f'{x} Not present in the list'


c = binarySearch(lst, x)
print(c)
