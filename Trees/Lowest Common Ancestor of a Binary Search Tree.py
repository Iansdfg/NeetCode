# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return found_candidit
        lca = self.dfs(root, p, q)
        return lca


    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        # return candidit
        if not root:
            return None 

        candidit = None 

        left_candidit = self.dfs(root.left, p, q)
        right_candidit = self.dfs(root.right, p, q)
        
        if left_candidit and right_candidit:
            candidit = root 
        elif left_candidit or right_candidit:
            candidit = left_candidit or right_candidit 

        if root == q or root == p:
            candidit = root

        return candidit
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return found_candidit
        lca, found_p, found_q = self.dfs(root, p, q)

        if found_p and found_q:
            return lca
        return None


    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        # return candidit, found_p, found_q
        if not root:
            return None, False, False 

        candidit = None 


        left_candidit, left_found_p, left_found_q = self.dfs(root.left, p, q)
        right_candidit, right_found_p, right_found_q = self.dfs(root.right, p, q)
        
        if left_candidit and right_candidit:
            candidit = root 
        elif left_candidit or right_candidit:
            candidit = left_candidit or right_candidit 

        if root == q or root == p:
            candidit = root

        found_p = left_found_p or right_found_p or root == p
        found_q = left_found_q or right_found_q or root == q

        return candidit, found_p, found_q
        
