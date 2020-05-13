import sys


def search_ceiling_of_a_number(arr, tar):
    start = 0
    end = len(arr) - 1
    if arr[end] < tar:
        return -1

    while start <= end:
        mid = start + (end - start) // 2
        n = arr[mid]
        print("start {0}, end {1}, mid {2}, current {3}".format(start, end, mid, n))

        if n == tar:
            return mid
        elif tar >= n:
            start = mid + 1
        elif tar < n:
            end = mid - 1

    return start


# def main():
#   print(search_ceiling_of_a_number([4, 6, 10], 6)) # 1
#   print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12)) # 4
#   print(search_ceiling_of_a_number([4, 6, 10], 17))
#   print(search_ceiling_of_a_number([4, 6, 10], -1))
#
#
# main()
