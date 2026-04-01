# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p, q):
            if not p and not q:
                return True
            elif (p is None) != (q is None):
                return False
            elif p.val != q.val:
                return False

            return same(p.left, q.left) and same(p.right, q.right)

        def traverse(p, q):
            if not p:
                return False
            
            return same(p, q) or traverse(p.left, q) or traverse(p.right, q)


        if not subRoot:
            return False

        return traverse(root, subRoot)

