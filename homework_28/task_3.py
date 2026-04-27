def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(alist, cutoff = 10):
    quick_sort_helper(alist, 0, len(alist) - 1, cutoff)

def quick_sort_helper(alist, first, last, cutoff):
    if first < last:
        if last - first + 1 <= cutoff:
            insertion_sort(alist, first, last)
            return

        split = partition(alist, first, last)

        quick_sort_helper(alist, first, split - 1, cutoff)
        quick_sort_helper(alist, split + 1, last, cutoff)

def partition(alist, first, last):
    pivot = alist[first]
    left = first + 1
    right = last

    done = False
    while not done:
        while left <= right and alist[left] <= pivot:
            left += 1
        while right >= left and alist[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]

    alist[first], alist[right] = alist[right], alist[first]
    return right

import random

arr = [random.randint(1, 100) for _ in range(20)]
arr2 = [random.randint(1, 100) for _ in range(5)]
quick_sort(arr, cutoff=10)
quick_sort(arr2, cutoff=10)

print(arr)
print(arr2)