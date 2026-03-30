# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        m_list = []
        while ptr1 and ptr2:
            low = ptr1.val
            if ptr1.val >= ptr2.val:
                low = ptr2.val
                ptr2 = ptr2.next
            else:
                ptr1 = ptr1.next
            m_list.append(low)
        
        while ptr1:
            m_list.append(ptr1.val)
            ptr1 = ptr1.next

        while ptr2:
            m_list.append(ptr2.val)
            ptr2 = ptr2.next
        
        dummy = ListNode(-1)
        curr = dummy
        for val in m_list:
            curr.next = ListNode(val)
            curr = curr.next
        list3 = dummy.next
        return list3