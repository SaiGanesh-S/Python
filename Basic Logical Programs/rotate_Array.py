# Problem Description -: Given an array Arr[ ] of N integers and a positive integer K.
#  The task is to cyclically rotate the array clockwise by K.

# Note: Keep the first of the array unaltered.


# clockwise rotation
def clock_rotate(arr):
    arr[:] = arr[-1:]+arr[:-1]
    return arr


# Anticlockwise rotation
def anti_clock_rotate(arr):
    arr[:] = arr[1:]+arr[:1]
    return arr


# main
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    k = int(input())
    if k > n:
        k = k % n
    for i in range(k):
        if i == k-1:
            #print("clockwise ", clock_rotate(arr))
            print("anit clockwise ", anti_clock_rotate(arr))
        else:
            # clock_rotate(arr)
            anti_clock_rotate(arr)
