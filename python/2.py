# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_str = ""
        num2_str = ""

        while l1 != None:
            num1_str = str(l1.val) + num1_str
            l1 = l1.next
        while l2 != None:
            num2_str = str(l2.val) + num2_str
            l2 = l2.next

        sum = int(num2_str) + int(num1_str)

        last = ListNode(int(str(sum)[0]),None)
        if len(str(sum))==1:
            return last

        for s in str(sum)[1:]:
            current = ListNode(int(s),last)
            last = current

        return current

