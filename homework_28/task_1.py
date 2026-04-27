def cocktail_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        end -= 1
        swapped = False

        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        start += 1

    return arr

if __name__ == '__main__':
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(cocktail_sort(unsorted_list))

'''
Алгоритм доцільний, коли:
- масив майже відсортований
- елементи можуть бути зміщені як на початку, так і в кінці
'''