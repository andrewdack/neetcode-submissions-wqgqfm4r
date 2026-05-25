func maxAreaOfIsland(grid [][]int) int {
    maxArea := 0

    for r := 0; r < len(grid); r++ {
        for c := 0; c < len(grid[r]); c++ {
            val := grid[r][c]
            if val == 1 {
                maxArea = max(maxArea, computeArea(r, c, grid))
            }
        }
    }
    return maxArea
}


func computeArea(r, c int, grid [][]int) int {
    if !isValid(r, c, grid) || grid[r][c] == 0 {
        return 0
    }

    areaSum := 0 // existing cell

    if grid[r][c] == 1 {
        areaSum += 1
        grid[r][c] = 0
    }
    areaSum += computeArea(r + 1 , c, grid)
    areaSum += computeArea(r - 1, c, grid)
    areaSum += computeArea(r, c + 1, grid)
    areaSum += computeArea(r, c - 1, grid)

    return areaSum
}

func isValid(r, c int, grid [][]int) bool {
    return (r >= 0 && r < len(grid) && c >= 0 && c < len(grid[r]))
}