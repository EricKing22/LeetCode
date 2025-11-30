from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.match = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dps(current, memory, memory_sum):
            memory.append(current)
            memory_sum += current.val

            if memory_sum == targetSum:
                if not current.left and not current.right:
                    self.match = True

            if current.left:
                dps(current.left, memory, memory_sum)
            if current.right:
                dps(current.right, memory, memory_sum)

            memory_sum -= memory[-1].val
            memory.pop()


        dps(root, [], 0)

        return self.match