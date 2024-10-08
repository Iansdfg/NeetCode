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


#比起return cadidit，不如直接return lca， 如果没找到就return none
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        found_p, found_q, lca = self.dfs(root,q,p)
        return lca

    def dfs(self, node, p, q):
        #return found_p, found_q, lca
        if not node:
            return False, False, None 

        left_found_p, left_found_q, left_lca = self.dfs(node.left, p, q)
        right_found_p, right_found_q, right_lca = self.dfs(node.right, p, q)

        if left_lca or right_lca:
            return True, True, left_lca or right_lca 

        found_p = left_found_p or right_found_p or node.val == p.val
        found_q = left_found_q or right_found_q or node.val == q.val

        if found_p and found_q:
            return found_p, found_q, node 

        return found_p, found_q, None 
        

        


        
