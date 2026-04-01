# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def postorder(p, q):
            if not p and not q:
                return True
            elif (p is None) != (q is None):
                return False
            elif p.val != q.val:
                return False

            return postorder(p.left, q.left) and postorder(p.right, q.right)

        def traverse(p, q):
            if not p:
                return False
            
            return traverse(p.left, q) or traverse(p.right, q) or postorder(p, q)

        return traverse(root, subRoot)

