from typing import List, Optional

class LinkNode:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional["LinkNode"] = None

class LinkedList:
    def __init__(self):
        self.head = LinkNode(-1)   # dummy/sentinel
        self.tail = self.head      # when empty, tail == dummy

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr = self.head.next      # first real node
        i = 0
        while curr is not None and i < index:
            curr = curr.next
            i += 1
        return curr.val if curr is not None else -1

    def insertHead(self, val: int) -> None:
        node = LinkNode(val)
        node.next = self.head.next
        self.head.next = node
        if self.tail is self.head:   # was empty
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = LinkNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        if index < 0:
            return False
        # prev = node BEFORE the one we remove; start at dummy
        prev = self.head
        i = 0
        while prev.next is not None and i < index:
            prev = prev.next
            i += 1
        if prev.next is None:        # out of bounds
            return False
        target = prev.next
        prev.next = target.next
        if target is self.tail:       # removed last node
            self.tail = prev
        return True

    def getValues(self) -> List[int]:
        out: List[int] = []
        curr = self.head.next        # skip dummy
        while curr is not None:
            out.append(curr.val)
            curr = curr.next
        return out
