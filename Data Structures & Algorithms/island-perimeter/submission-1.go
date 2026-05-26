var dir = [][2]int{ {-1, 0}, {1, 0}, {0, -1}, {0, 1} }
func islandPerimeter(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])
    var visited = make(map[[2]int]bool)


    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if grid[r][c] == 1 {
                return bfs(r, c, grid, visited)
            }
        }
    }
    return 0
}

func bfs(r, c int, grid [][]int, visited map[[2]int]bool) int {
    queue := [][2]int{{r, c}}
    visited[[2]int{r, c}] = true
    p := 0
    for len(queue) > 0 {
        cell := queue[0]
        queue = queue[1:]

        x, y := cell[0], cell[1]

        for _, d := range dir {
            nx, ny := x + d[0], y + d[1]
            
            if isPerim(nx, ny, grid) {
                p++
            } else if cell := [2]int{nx, ny}; !visited[cell] {
                visited[cell] = true
                queue = append(queue, cell)
            }
        }
    }
    return p
}

func isPerim(r, c int, grid [][]int) bool {
    return r < 0 || c < 0 || r >= len(grid) || c >= len(grid[0]) || grid[r][c] == 0
}
