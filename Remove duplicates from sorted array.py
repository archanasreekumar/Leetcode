https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=len(set(nums))
        nums[:]=[i for i in dict.fromkeys(nums)]
        return k