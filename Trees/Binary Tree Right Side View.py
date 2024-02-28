# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level = -1
            for _ in range(len(queue)):
                curr = queue.popleft()
                level = curr.val
                for next_node in [curr.left, curr.right]:
                    if next_node:
                        queue.append(next_node)
            res.append(level)
        
        return res

            
