# Definition for singly-linked list.
from typing import Optional
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        queue = deque([])

        while head:
            queue.append(head.val)
            head = head.next

        while len(queue) > 1:
            start = queue.popleft()
            end = queue.pop()
            if start != end:
                return False

        return len(queue) <= 1


