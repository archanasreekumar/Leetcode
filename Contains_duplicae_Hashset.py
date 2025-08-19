def get_duplicate_set(nums):
    out = set()

    for num in nums:
        if num in out:
            return True
        else:
            out.add(num)
    return False


def get_duplicate_set_len(nums):
    out_len = len(set(nums))
    in_len = len(nums)

    if out_len == in_len:
        return False
    return True


nums = [1, 21, 3, 22, 4, 30, 5]
print(get_duplicate_set(nums))
print(get_duplicate_set_len(nums))
