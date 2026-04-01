# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True

        def dfs(node):
            nonlocal balanced
            if not balanced:
                return 0
            if not node:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            d = abs(leftHeight - rightHeight)

            if d > 1:
                balanced = False
            
            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return balanced
        

