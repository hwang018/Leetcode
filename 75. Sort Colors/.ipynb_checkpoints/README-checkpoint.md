Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Idea:
Dutch National Flag problem
Use 3 pointers to track low medium high regions.
starting:
p0 = 0, boundary of 0 elements
p2 = end index, boundary of 2 elements
p1, current index, will be tested
each p1 will be tested to be 0 or 2, and exchange value with either p0 or p2.
