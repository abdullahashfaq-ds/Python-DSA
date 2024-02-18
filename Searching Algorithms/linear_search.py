def linear_search_iterative(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_recursive(arr, target, index=0):
    if index == len(arr):
        return -1

    if arr[index] == target:
        return index

    return linear_search_recursive(arr, target, index + 1)
