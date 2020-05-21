# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        If there is no cycle in the list, the fast pointer will eventually reach the end and we         can return false in this case.
        slow and fast pointers
        '''
        #if there are no cycle, the 2 pointers will never meet!
        if (head == None) or (head.next==None):
            return False
        #while loop keep exploring the next item
        slow = head
        fast = head.next
        while(slow!=fast):
            if (fast==None) or (fast.next==None):
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True