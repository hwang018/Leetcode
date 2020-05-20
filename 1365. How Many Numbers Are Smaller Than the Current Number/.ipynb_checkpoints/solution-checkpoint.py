class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        d = dict()
        for i,v in enumerate(sorted_nums):
            if v in d.keys():
                continue
            else:
                #it's a new element, store it's index
                #sorted array, its index is the number of elements smaller than it
                d[v]=i
        res = []
        for v in nums:
            res.append(d[v])
        return res