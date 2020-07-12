class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(list)
        for i,n in enumerate(nums):
            d[n].append(i)
        
        #then for each key in d, take combination of 2 from value list
        count = 0
        for k,v in d.items():
            length = len(v)
            if length >=2:
                c = math.comb(length, 2)
                count+=c
        return count