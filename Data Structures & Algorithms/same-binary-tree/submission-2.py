# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        pNodes = []
        qNodes = []
        
        def inorder(n, l):
            if n == None:
                l.append(n)
                return
            inorder(n.left, l)
            inorder(n.right, l)
            l.append(n.val)
        
        inorder(p, pNodes)
        inorder(q, qNodes)
        print(pNodes)
        print(qNodes)
        return pNodes == qNodes
            