class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #test one by one from 1 to sqrt(c)
        if c == 0:
            return True
        
        max_possible = int(math.sqrt(c))
        
        for i in range(1,max_possible+1):
            val1 = i**2
            val2 = c - val1
            
            if math.sqrt(val2) == int(math.sqrt(val2)):
                return True
            else:
                continue
            
        return False