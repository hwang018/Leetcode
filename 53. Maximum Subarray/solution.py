class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_global=max_current=nums[0]
        i = 1
        while i <= len(nums)-1:
            max_current = max(nums[i],max_current+nums[i])
            if max_current > max_global:
                max_global = max_current 
            i+=1                
        return max_global