class Solution:
    def balancedStringSplit(self, s: str) -> int:
        '''
        consider a random walk, encountering L +1
        R -1, then we can have the 2D chart        
        track the accumulated sum, if it's 0, means it's balanced
        '''
        res = []
        s_list = list(s)
        
        accum_sum = 0
        for i,s in enumerate(s_list):
            if s == 'L':
                accum_sum+=1
            elif s == 'R':
                accum_sum-=1
            if accum_sum == 0:
                #a balanced string occurred, note down it's index
                res.append(i)
        return len(res)