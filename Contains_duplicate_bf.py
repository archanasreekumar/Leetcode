class Containduplicate:
    def get_duplicate(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False

nums = [1,2,3,21,4,30,5]
cd = Containduplicate()
print(cd.get_duplicate(nums))