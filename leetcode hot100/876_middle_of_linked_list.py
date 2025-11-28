# Definition for singly-linked list.
import math
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        if not head:
            return None
        if not head.next:
            return head

        current = ListNode(head.val, head.next)
        while current.next:
            i += 1
            current = current.next

        mid = math.ceil(i / 2)

        ans = head
        for _ in range(0,mid-1):
            ans = ans.next

        return ans

