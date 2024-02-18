def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive_aux(arr, target, left, right):
    if left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive_aux(arr, target, mid + 1, right)
        else:
            return binary_search_recursive_aux(arr, target, left, mid - 1)

    return -1


def binary_search_recursive(arr, target):
    return binary_search_recursive_aux(arr, target, 0, len(arr) - 1)
