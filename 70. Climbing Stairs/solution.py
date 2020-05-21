class Solution:
    def climbStairs(self, n: int) -> int:
        #dynamic programming solution:
        #broken into subproblems, and it contains the optimal substructure property 
        '''
        one can reach ith step in 2 ways:
        1. taking 1 step from i-1 step
        2. taking 2 steps from i-2 step
        dp[i]=dp[i-1]+dp[i-2]

        '''
        dp =[0]*(n+1)
        #base conditions
        if n==1:
            return 1
        else:
            dp[1] = 1
            dp[2] = 2
            for i in range(3,n+1):
                dp[i]=dp[i-1]+dp[i-2]
            return dp[n]