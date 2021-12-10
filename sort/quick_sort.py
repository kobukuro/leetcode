import math


def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left


def quick_sort(arr, left, right):
    if left > right:
        return
    pivot = arr[math.floor((left + right) / 2)]
    index = partition(arr, left, right, pivot)
    if left < index - 1:
        quick_sort(arr, left, index - 1)
    if right > index:
        quick_sort(arr, index, right)


if __name__ == '__main__':
    arr = [8, 5, 3, 7, 10, 6, 2]
    left = 0
    right = len(arr) - 1
    quick_sort(arr, left, right)
    print(arr)
