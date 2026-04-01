# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0

        maxD = 0
        def dfs(node):
            nonlocal maxD
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right) 
            if node.left:
                leftHeight += 1
            if node.right:
                rightHeight += 1
            d = leftHeight + rightHeight
            maxD = max(d, maxD)
            return max(leftHeight, rightHeight)

        dfs(root)
        return maxD