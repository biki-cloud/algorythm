from typing import List

def counting_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    counts = [0] * (max_num + 1) # どの数字がいくつあるかのリストを作成
    result = [0] * len(numbers) # result

    for num in numbers:
        counts[num] += 1
    stas = []
    for i,v in enumerate(numbers):
        stas.append(i)
    stas.append(i+1)

    print(numbers)
    print(stas)
    print(counts)

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        result[counts[index] - 1] = numbers[i]
        counts[index] -= 1
        i -= 1

    print(result)


if __name__ == "__main__":
    # nums = [4, 3, 6, 2, 3, 4, 7]
    import random
    nums = [random.randint(0, 1000) for _ in range(100)]
    counting_sort(nums)