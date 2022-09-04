# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None:
            return
        
        def rightLeaf(node):
            curr = node
            while curr.right != None:
                curr= curr.right
            return curr
        
        self.flatten(root.right)
        
        if root.left != None:
            self.flatten(root.left)
            rightLeaf(root.left).right = root.right
            root.right = root.left
            root.left = None
