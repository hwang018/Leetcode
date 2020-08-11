Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Idea:
Using the idea of the solution, 
at each element, we can expand out, treating that element as the center of the potential palindrome substring.
So at each element, the cost to search for current anchored palindrome is O(n), there are n 
positions in total, so we have a O(n2) solution.

Edge case, above is assuming the element being the center of palindrome, requiring it to have odd-length
For even length palindrome, we need to manually shift by 1 position and test again.