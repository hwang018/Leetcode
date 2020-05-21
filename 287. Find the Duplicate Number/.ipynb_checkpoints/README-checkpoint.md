Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Idea:
Cannot alter the array
O(1) space required

Floyd's algorithm (2 pointers, fast and slow)
Call them tortoise and hare
phase 1: both starts from 0, hare twice as fast as tortoise
while xxx:
    this kind of operation creates something like linked list
    tortoise = nums[tortoise]
    then twice fast is like:
    hare = nums[nums[hare]]
    
    