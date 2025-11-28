# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        if head.val == head.next.val:
            while head.val == head.next.val:
                head = head.next
                if not head.next:
                    return None
            head = self.deleteDuplicates(head.next)

        else:
            head.next = self.deleteDuplicates(head.next)

        return head

