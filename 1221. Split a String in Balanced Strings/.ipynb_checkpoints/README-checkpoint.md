1221. Split a String in Balanced Strings

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.


Idea:

Thinking about this process as a random walk, loop once, if L: +1
if R: -1, track the accumulated sum.
At accum_sum = 0: means it's a viable balanced string. 
最后得到一个res list，包含所有的accum sum = 0 的index
有多少个element就有多少个minimum balanced string.