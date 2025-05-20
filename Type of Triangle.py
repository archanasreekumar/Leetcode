#https://leetcode.com/problems/type-of-triangle/

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        try:
            if len(nums)==3:
                pass
        except:
            print(f'invalid lenghth of {len(nums)}')
        
        if nums[0]==nums[1]==nums[2]:
            return "equilateral"
        if (nums[0]+nums[1]>nums[2]) and (nums[0]+nums[2]>nums[1]) and (nums[1]+nums[2]>nums[0]):
            if nums[0]!=nums[1] and nums[1]!=nums[2] and nums[0]!=nums[2]:
                return "scalene"
            else:
                return "isosceles"
        else:
            return "none"