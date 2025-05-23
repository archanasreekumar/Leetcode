https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=len(nums)-nums.count(val)
        # [:] helps to update the original list without  creating a new nums
        nums[:]=[i for i in nums if i!=val] 
        return k

        