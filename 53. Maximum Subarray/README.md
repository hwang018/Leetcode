Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Idea:
Kadane's algorithm, we consider at each index position, the max value of the subarray ending at current index will be:
M+nums[i] at each index i.
M is the max subarray sum value at previous index. 
Using dynamic programming to solve this.