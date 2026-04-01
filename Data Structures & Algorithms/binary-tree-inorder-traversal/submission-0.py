# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        def iot(node):
            if node:
                iot(node.left)
                nodes.append(node.val)
                iot(node.right)

        iot(root)
        return nodes