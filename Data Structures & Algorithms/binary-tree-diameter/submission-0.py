# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def diameterofBinaryTree(node):
            if node is None:
                return 0
            

            leftheight = diameterofBinaryTree(node.left)
            rightheight = diameterofBinaryTree(node.right)

            # update 

            self.diameter = max(self.diameter , leftheight + rightheight)

            return 1 + max(leftheight  , rightheight)
        
        diameterofBinaryTree(root)
        
        return self.diameter

    
        