import argparse
def main(arr):
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def arr2lst(arr):
        '''
        convert array to linked list
        :param arr:
        :return:
        '''
        dummy = curr = ListNode(0)
        for e in arr:
            curr.next = ListNode(e)
            curr = curr.next
        return dummy.next

    def middleNode(head: ListNode) -> ListNode:
        #create 2 pointers, fast is 2 times speed of slow
        slow = fast = head
        while fast and fast.next:
            #still have valid fast and its next pointer (not yet end list)
            slow = slow.next
            fast = fast.next.next
        return slow

    head = arr2lst(arr)
    print(middleNode(head).val)

    return None

if __name__ == "__main__":
    arr = [1,5,6,3,3,4,6,8]
    main(arr)
