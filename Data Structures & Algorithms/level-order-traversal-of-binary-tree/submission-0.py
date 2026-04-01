# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # make a list for each level
        # dequeue every node out the queue (the level) into the list
        # loop over the list and enqueue each child
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            level = []
            while len(queue) > 0:
                level.insert(0, queue.pop())
            
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # turn the nodes into vals
            for i in range(len(level)):
                level[i] = level[i].val

            res.append(level)

        return res
