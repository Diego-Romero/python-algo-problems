from typing import List


def find_max_in_bitonic_array(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return nums[left]


def main():
    print(find_max_in_bitonic_array([1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 6, 3, 2, 1]))  # 12
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2])) # 12
    print(find_max_in_bitonic_array([3, 8, 3, 1])) # 8
    print(find_max_in_bitonic_array([1, 3, 8, 12]))  # 12
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
