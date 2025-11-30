# Definition for a binary tree node.
from functools import total_ordering
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left = root.left
        right = root.right
        return max(1 + self.maxDepth(left), 1 + self.maxDepth(right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        left = root.left
        right = root.right
        left_height = self.maxDepth(left)
        right_height = self.maxDepth(right)

        if abs(left_height - right_height) <= 1:
            return self.isBalanced(left) and self.isBalanced(right)
        else:
            return False

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = root.left
        right = root.right
        max_length = self.maxDepth(left) + self.maxDepth(right)

        left_max = self.diameterOfBinaryTree(left)
        right_max = self.diameterOfBinaryTree(right)

        return max(left_max, right_max, max_length)

