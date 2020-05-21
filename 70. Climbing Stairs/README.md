You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Idea:
Bread into sub problems.
To reach step i, there are only 2 ways:
taking 1 step from i-1 or 2 steps from i-2
dp[i] = dp[i-1]+dp[i-2]
