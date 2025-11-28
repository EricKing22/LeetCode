# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        fast = head.next
        slow = head

        while fast.next or fast.next.next:
            if slow.val == fast.val:
                return True

            fast = fast.next.next
            slow = slow.next


        return False




