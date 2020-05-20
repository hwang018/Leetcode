class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        #just use a counter to store frequency, all frequency should be the same
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2