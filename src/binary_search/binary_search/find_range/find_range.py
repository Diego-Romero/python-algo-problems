from typing import List


def find_range_binary_search(arr: List[int], target: int, lookingForMax: bool) -> int:
    left = 0
    right = len(arr)
    key_index = -1

    while left <= right:
        mid = left + (right - left) // 2
        num = arr[mid]

        if target > num:
            left = mid + 1
        elif target < num:
            right = mid - 1
        else:
            # middle spot found
            key_index = mid
            if not lookingForMax:
                right = mid - 1
            else:
                left = mid + 1

    return key_index


def find_range(arr, key) -> List[int]:
    result = [- 1, -1]
    result[0] = find_range_binary_search(arr, key, False)
    result[1] = find_range_binary_search(arr, key, True)
    print(result)

    return result



def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
