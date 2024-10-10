# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None 

        root_val = preorder[0]
        root = TreeNode(root_val)

        if len(preorder) == 1:
            return root
        
        root_post = self.find_root_pos(root_val, inorder)

        left_preorder = preorder[1:root_post + 1]
        left_inorder = inorder[:root_post]
        right_preorder = preorder[root_post + 1:]
        right_inorder = inorder[root_post + 1:]

        build_left = self.buildTree(left_preorder, left_inorder)
        build_right = self.buildTree(right_preorder, right_inorder)

        root.left = build_left
        root.right = build_right
        return root

    def find_root_pos(self, val, arrary):
        for i in range(len(arrary)):
            if arrary[i] == val:
                return i
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, inorder)

    def dfs(self, preorder, inorder):
        if not inorder or not preorder:
            return None 

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        node_val = preorder[0]
        inorder_pos =self.find_pos(node_val, inorder)

        inorder_left = inorder[:inorder_pos]
        inorder_right = inorder[inorder_pos+1:]
        preorder_left = preorder[1:inorder_pos+1]
        preorder_right = preorder[inorder_pos+1:]

        left_child = self.dfs(preorder_left, inorder_left)
        right_child = self.dfs(preorder_right, inorder_right)

        node = TreeNode(node_val)
        node.left = left_child
        node.right = right_child

        return node

    def find_pos(self, val, inorder):
        if val not in inorder:
            return 0
        return inorder.index(val)


        
