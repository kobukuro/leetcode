# Runtime: O(n log(n)) average, O(n^2) worst case. Memory: O(log(n)).
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
    """
        Sorts an array using the Quick Sort algorithm.

        :param arr: The array to be sorted.
        :param left: The starting index of the subarray to be sorted.
        :param right: The ending index of the subarray to be sorted.

        :return:
            None, The original array is sorted in-place.

    """
    """
    When the left pointer is equal to the right pointer, 
    it means that this subarray has only one element, 
    so there is no need to sort it (it is already sorted). 
    In that case, we can simply return. 
    When the left pointer is greater than the right pointer, 
    it means that it is not a valid subarray, so we can also return directly.
    """
    if left >= right:
        return
    pivot = arr[math.floor((left + right) / 2)]
    index = partition(arr, left, right, pivot)
    quick_sort(arr, left, index - 1)
    quick_sort(arr, index, right)


if __name__ == '__main__':
    arr = [8, 5, 3, 7, 10, 6, 2]
    left = 0
    right = len(arr) - 1
    quick_sort(arr, left, right)
    print(arr)
