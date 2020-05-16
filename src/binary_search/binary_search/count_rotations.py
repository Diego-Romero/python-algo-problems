from typing import List


def count_rotations(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        # print(mid, arr[mid])

        if mid > 0 and arr[mid - 1] > arr[mid]:
            return mid
        elif arr[mid] > arr[right]: # if the middle is bigger than the end we need to look in the right side
            left = mid + 1
        else:
            right = mid - 1

    return 0

def main():
    # print(count_rotations([10, 15, 1, 3, 8])) # 2
    # print(count_rotations([4, 5, 7, 9, 10, -1, 2])) # 5
    # print(count_rotations([1, 3, 8, 10])) # 0
    # print(count_rotations([9, 1, 2, 3, 4, 5])) # 0
    # print(count_rotations([])) # 0
    print(count_rotations([3,3,7,3])) # 0


main()