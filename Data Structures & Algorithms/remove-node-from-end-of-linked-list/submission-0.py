# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        rem_i = size - n
        if rem_i == 0:
            head = head.next
            return head
        if rem_i < 0:
            return head
        
        prev = head
        curr = head
        i = 0
        while i < rem_i:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = curr.next
        return head