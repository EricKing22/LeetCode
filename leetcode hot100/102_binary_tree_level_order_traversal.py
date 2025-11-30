# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [(root, 0)]

        all_nodes = [(root, 0)]
        def bfs():
            while len(q) > 0:

                node, level = q.pop(0)
                if node.left:
                    q.append((node.left, level+1))
                    all_nodes.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level+1))
                    all_nodes.append((node.right, level + 1))


        bfs()

        ans = []
        row = [all_nodes[0][0].val]
        for i in range(1, len(all_nodes)):
            if all_nodes[i][1] == all_nodes[i-1][1]:
                row.append(all_nodes[i][0].val)
            else:
                ans.append(row)
                row = [all_nodes[i][0].val]
        ans.append(row)
        return ans




