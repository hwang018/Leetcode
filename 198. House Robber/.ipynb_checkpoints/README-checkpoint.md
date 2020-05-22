You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Idea:
Typical dynamic programming problem. The answer can be backtracked
Max profit at the end of the houses = max(P(i-2)+A[i],P(i-1))
Choice between rob i-2 th house and current ith house, versus robbing i-1 th house.

To solve dp problem, think of doing a series of states.
e.g. dp = [0] * size(input_array)
we can pre-fill dp array with 0 in this question, each step i, will depend on i-2 and i-1, and A[i].
