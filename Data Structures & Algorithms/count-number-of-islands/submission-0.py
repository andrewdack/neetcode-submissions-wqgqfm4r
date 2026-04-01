class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands += 1
                    self.DFSremove(r, c, grid)

        return islands

    def DFSremove(self, r, c, grid):
        # print(r, c)
        if grid[r][c] == "1":
            # up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for d in directions:
                newR = r + d[0]
                newC = c + d[1]
                if self.onBoard(newR, newC, grid):
                    # print(newR, newC)
                    grid[r][c] = "0"
                    self.DFSremove(newR, newC, grid)

            # mark as 0 
    
    def onBoard(self, r, c, grid):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
        