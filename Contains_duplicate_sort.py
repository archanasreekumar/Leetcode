def get_duplicate(nums):
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i-1]:
            return True
    return False



nums = [1,3,101,6,4,16,10,8]
print(get_duplicate(nums))