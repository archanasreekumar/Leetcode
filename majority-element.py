#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_set=set(nums)
        count_dict={}
        for i in num_set:
            count_dict[i]=nums.count(i)
        return max(count_dict,key=count_dict.get)
        
        
        