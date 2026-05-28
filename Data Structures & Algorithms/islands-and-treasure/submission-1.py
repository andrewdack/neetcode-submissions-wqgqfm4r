class Solution:
    # get position ofeach chest
    # level by level bfs from the chest and fill each land cell with distance
    # only replace land cell with existing distance
    # if new distance < existing distance
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def isValid(r, c, grid):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])

        DIRS = [[1,0], [-1,0], [0,1], [0,-1]]

        treasure = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    treasure.add((r,c))

        queue = deque() 
        for r, c in treasure:
            queue.append((r, c))
        # level by level bfs
        distance = 1
        while queue:
            size = len(queue)

            # canMove = False
            print(grid)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in DIRS:
                    nr, nc = dr + r, dc + c
                    if (isValid(nr, nc, grid) and
                    (grid[nr][nc] > 1000 or grid[nr][nc] > grid[r][c])):
                        # canMove = True
                        
                        grid[nr][nc] = distance
                        queue.append((nr, nc))
            
            distance += 1

            


