Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Idea: 
Typical dp problem, similar to question 53 (max sum subarray)
The solution will be either:
current max length nonrepeating subarray,
or current val + current max length nonrepeating subarray.
