# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.bst_iterator(root, k)
        return res

    def bst_iterator(self, root, k):
        dummy = TreeNode(-1)
        dummy.right = root
        stack = [dummy]
        res = -1
        for _ in range(k+1):
            curr = stack.pop()
            res = curr.val
            if curr.right:
                curr = curr.right
                stack.append(curr)
                while curr.left:
                    curr = curr.left
                    stack.append(curr)
        return res 

