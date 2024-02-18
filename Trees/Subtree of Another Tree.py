# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        return self.dfs(root, subRoot)

    def dfs(self, root, subRoot):
        if not root:
            return False 

        left_is_sub = self.dfs(root.left, subRoot)
        right_is_sub = self.dfs(root.right, subRoot)
        curr_is_sub = False
        if self.is_same_tree(root, subRoot):
            curr_is_sub = True 

        return left_is_sub or right_is_sub or curr_is_sub

    

    def is_same_tree(self, a, b):
        if not a and not b:
            return True 
        if not a or not b:
            return False 

        left_is_same = self.is_same_tree(a.left, b.left)
        right_is_same = self.is_same_tree(a.right, b.right)
        if left_is_same and right_is_same:
            return a.val == b.val 

        return False 


        
