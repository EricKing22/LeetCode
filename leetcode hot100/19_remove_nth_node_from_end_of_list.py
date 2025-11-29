from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q = [head]

        if not head or not head.next:
            return None
        current = ListNode(head.val, head.next)
        while current.next:
            current = current.next
            if len(q) <= n:
                q.append(current)
            else:
                q.pop(0)
                q.append(current)

        if q[-n] == head:
            return head.next

        if len(q) < 3:
            q[0].next = None
        else:
            q[-n-1].next = q[-n+1]

        return head