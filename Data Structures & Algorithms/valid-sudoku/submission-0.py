class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {i: set() for i in range(10)}
        colMap = {i: set() for i in range(10)}
        squareMap = {i: set() for i in range(10)}
        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == ".":
                    continue
                rowSet = rowMap[r]
                colSet = colMap[c]


                squareIndex = (r // 3) * 3 + (c // 3)
                squareSet = squareMap[squareIndex]

                if val in rowSet or val in colSet or val in squareSet:
                    return False
                
                # add val to seen
                rowSet.add(val)
                colSet.add(val)
                squareSet.add(val)

        return True