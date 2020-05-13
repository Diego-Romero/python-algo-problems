import math
from typing import Dict, List


def binary_search(arr: List[int], target: int):
    start = 0
    end = len(arr) - 1

    isAscending = True
    if arr[start] > arr[end]:
        isAscending = False

    while start <= end:
        mid = start + (end - start) // 2
        cur = arr[mid]

        if cur == target:
            return mid

        if isAscending:
            if target > cur:
                start = mid + 1
            elif target < cur:
                end = mid - 1
        else:
            if target > cur:
                end = mid - 1
            elif target < cur:
                start = mid + 1

    return -1


# def binary_search_helper(arr: List[int], start: int, end: int, target: int):
#     if start > end:
#         return -1
#     mid = start + (end - start) // 2
#     cur = arr[mid]
#     if cur == target:
#         return mid
#     elif target > cur:
#         return binary_search_helper(arr, mid + 1, end, target)
#     else:
#         return binary_search_helper(arr, start, mid - 1, target)
#
#
# def binary_search(arr: List[int], target: int):
#     return binary_search_helper(arr, 0, len(arr) - 1, target)


def main():
    print(binary_search([4, 6, 10], 10))  # 2
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))  # 4
    print(binary_search([10, 6, 4], 10))  # 0
    print(binary_search([10, 6, 4], 4)) # 2


main()
