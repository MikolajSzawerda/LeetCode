from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        res = head
        parent = None
        target = head
        i = 0
        while head and i < n:
            head = head.next
            i += 1
        while head:
            parent = target
            target = target.next
            head = head.next
        if parent:
            parent.next = target.next
        else:
            res = target.next
        return res
