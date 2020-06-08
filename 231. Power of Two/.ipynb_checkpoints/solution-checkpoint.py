class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x<n:
            x*=2 
            
        if x != n:
            return False
        else:
            return True