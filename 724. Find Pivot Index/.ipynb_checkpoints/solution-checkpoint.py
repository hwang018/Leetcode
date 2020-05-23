class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        for i,v in enumerate(nums):
            total_sum-=v
            if left_sum == total_sum:
                return i
            else:
                left_sum+=v
                continue
        return -1