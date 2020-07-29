Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

 

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Idea:
First to sort the arr.
Corner case: len(arr) = 1
if more than 2 elements, we can maintain a moving window of size 2.
Compare i and i-1 position to test if all differences are the same.