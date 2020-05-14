def binary_search(arr, key, find_max):
    key_index = -1
    left, right = 0, len(arr) - 1

    while left <= right:
        pivot = left + (right - left) // 2
        print(pivot)
        if key > arr[pivot]:
            left = pivot + 1
        elif key < arr[pivot]:
            right = pivot - 1
        else:
            # we have found the key
            key_index = pivot
            # print(key_index)
            if find_max:
                left = pivot + 1
            else:
                right = pivot - 1

    return key_index


def find_range(arr, key):
    result = [- 1, -1]
    result[0] = binary_search(arr, key, False)
    if result[0] == -1:
        return result
    result[1] = binary_search(arr, key, True)
    return result


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    # print(find_range([1, 3, 8, 10, 15], 10))
    # print(find_range([1, 3, 8, 10, 15], 12))


main()
