# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        if not root:
            return None

        values = []

        def dfs(current_node):

            if current_node.left:
                dfs(current_node.left)

            values.append(current_node.val)

            if current_node.right:
                dfs(current_node.right)


        dfs(root)

        values.sort()

        ans = 1e3
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i-1])

        return ans
