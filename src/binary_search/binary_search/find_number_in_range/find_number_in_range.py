import sys


def find_range(arr, key):
    result = [- 1, -1]

    left, right = 0, len(arr)
    min_left = float("inf")
    max_right = float("-inf")

    while left <= right:
        # need to find when it stops being smaller
        pivot = left + (right - left) // 2
        cur = arr[pivot]

        # if cur == key:



    return result


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    # print(find_range([1, 3, 8, 10, 15], 10))
    # print(find_range([1, 3, 8, 10, 15], 12))


main()
