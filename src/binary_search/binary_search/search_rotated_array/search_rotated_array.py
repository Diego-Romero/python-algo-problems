import math
from typing import List


def find_max(arr: List[int]) -> int:
    start = 0
    end = len(arr) - 1

    max_num = arr[start]
    max_index = 0

    while start < end:
        mid = start + (end - start) // 2
        mid_value = arr[mid]
        # we need to know if we need to go left or right by checking at far end of each side
        left = arr[start]
        right = arr[end]
        # print(mid, mid_value, left, right)
        # print("----")
        if mid_value > arr[mid + 1]:
            return mid
        if arr[mid - 1] > mid_value:
            return mid - 1
        elif left > arr[mid] and left > right:  # we def need to go left
            end = mid - 1
            if mid_value > max_num:
                max_num = max(max_num, mid_value)
                max_index = mid
        elif right > arr[mid] and right > left:
            start = mid + 1
            if mid_value > max_num:
                max_num = max(max_num, mid_value)
                max_index = mid
        else:
            # print("in else")
            start = mid
            if mid_value > max_num:
                max_num = max(max_num, mid_value)
                max_index = mid

    return max_index


def binary_search(arr, key, start_index, end_index) -> int:
    # print(start_index, end_index)
    start = start_index
    end = end_index

    while start <= end:
        mid = start + (end - start) // 2

        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        else:
            return mid

    return -1


def search_rotated_array(arr, key):
    # need to find max, which is where the array has rotated, from here we can trigger a binary search
    max_index = find_max(arr)
    print("max index: ", max_index)
    find_right = binary_search(arr, key, max_index + 1, len(arr) - 1)  # the numbers will go in ascendant order
    if find_right != -1:
        return find_right
    else:
        # need to look at the left side
        find_left = binary_search(arr, key, 0, max_index)

        if find_left != -1:
            return find_left

    return -1

def search_rotated_array_single_pass(arr, key):
    start = 0
    end = len(arr)

    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid

        if arr[start] <= arr[mid]: # left side is sorted
            if arr[start] <= key < arr[mid]: # is in this range
                end = mid - 1
            else: # is not in this range
                start = mid + 1
        else:
            if key > arr[mid] and key <= arr[end]: # the key is in the right side
                start = mid + 1
            else: # is not in this range
                end = mid - 1

    return -1



def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))  # max index 1, return 1
    print(search_rotated_array([15, 1, 3, 8, 10], 10))  # max index 0, return 4
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 2))  # max index: 4, 6
    print(search_rotated_array([5,6,7,9,11,1,2,3,4], 6)) # max index 4, return index 1
    print(search_rotated_array([4,5,6,7,0], 10)) # max index 3, return -1
    print(search_rotated_array([2,3,4,5,20,30,40,1], 10)) # max index 6, return -1


main()
