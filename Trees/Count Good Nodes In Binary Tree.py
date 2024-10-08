# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = self.dfs(root, float('-inf'))
        return cnt

    def dfs(self, root: TreeNode, max_val: int):
        if not root:
            return 0

        max_val = max(max_val, root.val)
        left_cnt, right_cnt = 0, 0
        if root.left:
            left_cnt = self.dfs(root.left, max_val)
        if root.right:
            right_cnt = self.dfs(root.right, max_val)
        
        cnt = left_cnt + right_cnt
   
        if root.val >= max_val:
            cnt += 1 
        return cnt
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good_cnt = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, float('-inf'))
        return self.good_cnt

    def dfs(self, node, max_val):
        if node.val >= max_val:
            self.good_cnt += 1 
        max_val = max(max_val, node.val)

        for next_node in [node.left, node.right]:
            if not next_node:
                continue 
            self.dfs(next_node, max_val)

            



        
        
