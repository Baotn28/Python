def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1

    return count

print(list_count_4([1, 6, 4, 7, 2, 4, 3]))