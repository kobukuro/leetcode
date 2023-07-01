# Runtime: O(n log(n)) average, O(n^2) worst case. Memory: O(log(n)).


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def qs(arr, left, right):
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
    it means that it is empty subarray, so we can also return directly.
    """
    if left >= right:
        return
    p = partition(arr, left, right)
    qs(arr, left, p - 1)
    qs(arr, p + 1, right)


def quick_sort(arr):
    qs(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    a1 = [3, 2, 1]
    a2 = [1, 2, 3]
    a3 = []
    a4 = [3, 1, -1, 0, 2, 5]
    a5 = [2, 2, 1, 1, 0, 0, 4, 4, 2, 2, 2]
    a6 = [0]
    a7 = [3, -2, -1, 0, 2, 4, 1]
    a8 = [1, 2, 3, 4, 5, 6, 7]
    a9 = [2, 2, 2, 2, 2, 2, 2]
    quick_sort(a1)
    quick_sort(a2)
    quick_sort(a3)
    quick_sort(a4)
    quick_sort(a5)
    quick_sort(a6)
    quick_sort(a7)
    quick_sort(a8)
    quick_sort(a9)
    assert a1 == [1, 2, 3]
    assert a2 == [1, 2, 3]
    assert a3 == []
    assert a4 == [-1, 0, 1, 2, 3, 5]
    assert a5 == [0, 0, 1, 1, 2, 2, 2, 2, 2, 4, 4]
    assert a6 == [0]
    assert a7 == [-2, -1, 0, 1, 2, 3, 4]
    assert a8 == [1, 2, 3, 4, 5, 6, 7]
    assert a9 == [2, 2, 2, 2, 2, 2, 2]
    print("If you didn't get an assertion error, this program has run successfully.")
