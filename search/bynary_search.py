import os
from typing import List, NewType

IndexNum = NewType("IndexNum", int)


def linear_search(numbers: List[int], value: int) -> int:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


def binary_search(numbers: List[int], value: int) -> int:
    left, right = 0, len(numbers) - 1
    while left <= right:
        print('###############')
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1



def recurcible_binary_search(numbers: List[int], value: int) -> IndexNum:
    def _recurcible_binary_search(numbers: List[int], value: int,
                                  left: IndexNum, right: IndexNum) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _recurcible_binary_search(numbers, value, mid + 1, right)
        else:
            return _recurcible_binary_search(numbers, value, 0, mid - 1)

    return _recurcible_binary_search(numbers, value, 0, len(numbers) - 1)


if __name__ == '__main__':
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    # print(binary_search(nums, 15))
    print(recurcible_binary_search(nums, 15))
