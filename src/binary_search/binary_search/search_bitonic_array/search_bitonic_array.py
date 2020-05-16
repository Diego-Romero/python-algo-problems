from typing import List


def binary_search(arr, key, start_index: int, end_index: int) -> int:
    start = start_index
    end = end_index
    reverse = arr[start] > arr[end]

    # print(start, end)
    while start <= end:
        mid = start + (end - start) // 2

        if reverse:
            if key < arr[mid]:
                start = mid + 1
            elif key > arr[mid]:
                end = mid - 1
            else:
                return mid
        else:
            if key > arr[mid]:
                start = mid + 1
            elif key < arr[mid]:
                end = mid - 1
            else:
                return mid

    return -1


def search_bitonic_array(arr: List[int], key: int) -> int:
    max_index = find_max_index(arr)
    # print(max_index)
    right = binary_search(arr, key, max_index, len(arr) - 1)
    if right != -1:
        return right
    else:
        left = binary_search(arr, key, 0, max_index)
        if left != - 1:
            return left
        else:
            return -1


    # need to trigger a binary search onto each side
    # right =


def find_max_index(arr: List[int]) -> int:
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid + 1] > arr[mid]:  # we want to move to the right
            start = mid + 1
        else:
            end = mid

    return start


def main():
    # testing reverse binary search
    # print(binary_search_reverse([10, 8, 6, 4, 3, 2], 3, 0)) # 4
    # print(binary_search_reverse([10, 8, 6, 4, 3, 2], 10, 0)) # 0
    # print(binary_search_reverse([10, 8, 6, 4, 3, 2], 6, 0)) # 2

    print(search_bitonic_array([1, 3, 8, 4, 3], 4)) # 3
    print(search_bitonic_array([3, 8, 3, 1], 8)) # 1
    print(search_bitonic_array([1, 3, 8, 12], 12)) # 3
    print(search_bitonic_array([10, 9, 8], 10)) # 0
    print(search_bitonic_array([10,20,30,40,50,45,35,25,15], 30)) # 2


main()
