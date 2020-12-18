from typing import List


# 隣の値と大きさを比較し入れ替えて行く
def cooktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swappend = True
    start = 0
    end = len_numbers - 1
    while swappend:
        swappend = True
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swappend = True

        if not swappend:
            break

        swappend = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swappend = True

        start = start + 1

    return numbers


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 1000) for i in range(100)]
    print(cooktail_sort(nums))