class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        counts = Counter(arr)
        res = []        
        for v in arr:
            if v == counts[v]:
                res.append(v)
        if len(res) >0:
            return max(res)
        else:
            return -1