# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        countGood = 0

        def dfs(node, maxVal):
            nonlocal countGood
            
            if not node:
                return
            
            newMax = maxVal
            if node.val >= maxVal:
                countGood += 1
                newMax = node.val
            
            dfs(node.left, newMax)
            dfs(node.right, newMax)

        
        dfs(root, root.val)
        return countGood