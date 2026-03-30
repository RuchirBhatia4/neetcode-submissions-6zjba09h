# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # itr = head
        # while itr and itr.next:
        #     curr = itr.next
        #     prev = itr
        #     while curr.next:
        #         prev = curr
        #         curr = curr.next
        #     a = curr.val
        #     prev.next = None
        #     newNode = ListNode(a)
        #     b = itr.next
        #     itr.next = newNode
        #     newNode.next = b
        #     itr = b

        stack = []
        curr = head
        while curr is not None:
            stack.append(curr)
            curr = curr.next
        
        a = head
        while a is not None:
            lastNode = stack.pop()
            nxt = a.next
            if lastNode == nxt or lastNode == a:
                lastNode.next = None
                break
            a.next = lastNode
            lastNode.next = nxt
            a = nxt
