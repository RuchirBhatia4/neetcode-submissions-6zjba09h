# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        digi_cnt = 1
        while l1:
            n1 += l1.val * digi_cnt
            l1 = l1.next
            digi_cnt *= 10

        n2 = 0
        digi_cnt = 1
        while l2:
            n2 += l2.val * digi_cnt
            l2 = l2.next
            digi_cnt *= 10

        n3 = n1 + n2

        if n3 == 0:
            return ListNode(0)

        l = []
        while n3:
            l.append(n3 % 10)
            n3 //= 10

        head = ListNode(l[0])
        tail = head
        for data in l[1:]:
            tail.next = ListNode(data)
            tail = tail.next

        return head