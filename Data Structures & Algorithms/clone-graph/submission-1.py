"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def printNode(node):
            print(f"val:{node.val}, neighbors:{node.neighbors}")
        if not node:
            return None

        # bfs to copy the graph USE POPLEFT
        queue = deque()
        queue.append(node)

        copyNode = Node(node.val, neighbors=[])
        copyMap = {} # map of orig node to cloned node
        copyMap[node] = copyNode
        while queue:
            for _ in range(len(queue)):
                curNode = queue.popleft()
                for neighbor in curNode.neighbors:
                    curCopyNode = copyMap[curNode]
                    if neighbor in copyMap:
                        curCopyNode.neighbors.append(copyMap[neighbor])
                    else:
                        copyMap[neighbor] = Node(neighbor.val, [])
                        curCopyNode.neighbors.append(copyMap[neighbor])
                        queue.append(neighbor)
        
        return copyNode

        