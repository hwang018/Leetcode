Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

Example 1:

Input: A = "ab", B = "ba"
Output: true

Idea:
Lots of corner cases to consider, especially empty input string
Use a list to store all the different positions and their values.
Only if 2 differences exist and by swapping it solves the differences, can we say it's a buddy string.