def merge(arr1, arr2):
    combined_arr = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            combined_arr.append(arr1[i])
            i += 1
        else:
            combined_arr.append(arr2[j])
            j += 1

    combined_arr += arr1[i:]
    combined_arr += arr2[j:]

    return combined_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid_index = len(arr)//2

    left = merge_sort(
        arr[:mid_index]
    )
    right = merge_sort(
        arr[mid_index:]
    )

    return merge(left, right)
