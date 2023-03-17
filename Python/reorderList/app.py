from typing import *

class ListNode:
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        rev = None

        while curr:
            n = curr.next
            curr.next = rev
            rev = curr
            curr = n

        forward = head

        while rev:
            n = forward.next
            forward.next = rev
            n2 = rev.next
            rev.next = n
            forward = n
            rev = n2
