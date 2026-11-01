# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root):

        def solve(node):

            if node is None:
                return 0

            lefth = solve(node.left)
            if lefth == -1:
                return -1

            righth = solve(node.right)
            if righth == -1:
                return -1

            if abs(lefth - righth) > 1:
                return -1

            return 1 + max(lefth, righth)

        x = solve(root)
        return x != -1
   
        
        