# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        res = self.dfs(p, q)
        return res

    def dfs(self, p, q):
        if not q and not p:
            return True 
        if not q or not p:
            return False
        left_is_same = self.dfs(p.left, q.left)
        right_is_same = self.dfs(p.right, q.right)

        if left_is_same == False or right_is_same == False:
            return False

        return q.val == p.val 
        
