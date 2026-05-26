class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # add all rotten oranges to the queue        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.appendleft((r, c))
        
        mins = 0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        temp_queue = deque()
        while len(queue) > 0:
            # spread each orange in the queue
            # then increment the minute
            r, c = queue.pop()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if self.canInfect(nr, nc, grid):
                    temp_queue.appendleft((nr, nc))
                    grid[nr][nc] = 2
                        
            if len(queue) == 0:
                mins += 1
                # refill queue
                while temp_queue:
                    queue.appendleft(temp_queue.pop())
                
        # check for any fresh oranges
        for row in grid:
            for cell in row:
                if cell == 1:
                    return -1
                
        return mins - 1 if mins != 0 else 0
    
    def canInfect(self, r, c, grid):
        return (
            r >= 0 and c>=0 and
            r < len(grid) and c < len(grid[0])
            and grid[r][c] == 1
        )