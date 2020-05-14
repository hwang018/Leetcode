# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #create 2 pointers, fast is 2 times speed of slow
        slow = fast = head
        while fast and fast.next:
            #still have valid fast and its next pointer (not yet end list)
            slow = slow.next
            fast = fast.next.next
        return slow
        