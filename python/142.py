# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head
        if not head or not head.next:
            return None
        else:
            fast = head.next.next
            slow = slow.next

        while fast!=slow:
            if not fast or not fast.next: return None
            slow = slow.next
            fast = fast.next.next

        fast = head
        while fast!=slow:
            slow = slow.next
            fast = fast.next

        return slow




