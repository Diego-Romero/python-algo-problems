import math


def search_min_diff_element(arr, target):
    print("target", target)
    diff = math.inf
    abs_n = math.inf

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        n = arr[mid]

        current_diff = abs(target - n)
        # print(n, current_diff, abs_n)

        if current_diff < diff:
          # print("setting current dif to", current_diff)
          abs_n = n
          diff = current_diff

        if target > n:
            left = mid + 1
        elif target < n:
            right = mid - 1
        else:
            return n

    # if (arr[left] - target) < (target - arr[right]):
    #     return arr[left]
    # return arr[right]

    return abs_n


def main():
    print(search_min_diff_element([4, 6, 10], 7))  # should return 6
    print(search_min_diff_element([4, 6, 10], 4))  # return 4
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))  # return 10
    print(search_min_diff_element([4, 6, 10], 17))  # return 10


main()
