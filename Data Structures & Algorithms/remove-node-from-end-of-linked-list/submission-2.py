# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1
        steps = size - n - 1
        if n == size:
            return head.next
        curr = head
        for _ in range(steps):
            curr = curr.next
        curr.next = curr.next.next
        return head

