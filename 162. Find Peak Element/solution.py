class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_ind = len(nums)-1
        res = []
        for i,v in enumerate(nums):
            if i<max_ind and i>0:
                # not reach end yet, have next val
                v1 = nums[i-1] < v 
                v2 = v > nums[i+1]
                val = v1 and v2
                res.append(val)
            else:
                res.append(False)
        # find indices with True as value
        indices = [i for i, x in enumerate(res) if x == True]
        
        if len(indices)>=1:
            return indices[0]
        else:
            return nums.index(max(nums))