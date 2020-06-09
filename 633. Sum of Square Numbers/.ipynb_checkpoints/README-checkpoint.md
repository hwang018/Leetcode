Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Idea:
Since we know c will be larger than a or b
the biggest possible value for a or b is sqrt(c)
therefore we can loop through 1 to sqrt(c), namly O(sqrt(n)) time complexity
to test out each case