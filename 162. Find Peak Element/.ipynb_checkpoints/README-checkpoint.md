A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Idea, O(n) solution:
We use a window of 3 elements, to test and label each position, to see if it's a peak.
After looping through n elements, we return one of the potential index. If not a single position satisfies,
we just return the index of max value in array to satisfy: bigger than all neighbours. 