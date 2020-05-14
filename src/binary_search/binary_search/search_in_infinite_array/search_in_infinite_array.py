import math
import sys
from typing import List


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader: ArrayReader, key: int) -> int:
    left = 0
    right = 1

    # start from the lower half to get right first
    while reader.get(right) < key:
        new_start = right + 1
        right += (right - left + 1) * 2
        left = new_start

    # print("right found: ", right)
    return binary_search(reader, key, left, right)


def binary_search(reader: ArrayReader, key: int, left, right) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        current = reader.get(mid)

        if key > current:
            left = mid + 1
        elif key < current:
            right = mid - 1
        else:
            return mid

    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()
