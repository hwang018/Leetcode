Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Idea:
Given a linked list, remove all duplicated adjaent nodes
always let curr = head as start,
then loop till tail of list
if curr.val == curr.next.val:
    curr.next = curr.next.next
else:
    #move forward the curr pointer
    curr = curr.next
    