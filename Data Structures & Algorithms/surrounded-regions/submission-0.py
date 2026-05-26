class Solution:
    def solve(self, board: List[List[str]]) -> None:
        borderCells = self.getBorderCells(board)

        # mark nonsurrounded cells
        for r, c in borderCells:
            if board[r][c] == 'O':
                self.markNonSurrounded(r, c, board)
        
        # second pass
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
        


    def markNonSurrounded(self, r, c, board):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != "O":
            return

        board[r][c] = '#'
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            self.markNonSurrounded(r + dr, c + dc, board)

    def getBorderCells(self, board):
        cells = []
        for c in range(len(board[0])):
            if board[0][c] == 'O':
                cells.append((0, c))
            if board[len(board) - 1][c] == 'O':
                cells.append((len(board) - 1, c))

        for r in range(1, len(board) - 1):
            if board[r][0] == 'O':
                cells.append((r, 0))

            if board[r][len(board[0]) - 1] == 'O':
                cells.append((r, len(board[0]) - 1))

        return cells