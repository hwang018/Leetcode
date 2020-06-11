class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        #sort everything in pair
        sorted_doms = [sorted(a) for a in dominoes]        
        str_dominoes = ["".join([str(integer) for integer in a]) for a in sorted_doms]
        from collections import Counter
        from math import comb
        
        counted = Counter(str_dominoes)
        
        res = 0
        
        for val in counted.values():
            if val>=2:
                res+=comb(val,2)
            else:
                continue
        return res
                