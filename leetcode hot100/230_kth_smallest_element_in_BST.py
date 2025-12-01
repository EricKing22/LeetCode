# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return None

        ans = []

        def dfs(current_node):

            if current_node.left:
                dfs(current_node.left)

            ans.append(current_node.val)

            if current_node.right:
                dfs(current_node.right)



        dfs(root)
        ans.sort()
        return ans[k-1]



