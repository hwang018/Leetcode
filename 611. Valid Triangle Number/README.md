Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:

Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Idea:
Only 1 condition to make a valid triangle: longest edge > sum of the other 2 edges.
We treate each edge as longest edge, and find the number of valid triangles in that condition.
Note the solution has a typical way of looping through array and find sum equal to certain value.(innder while loop, using left right pointers)