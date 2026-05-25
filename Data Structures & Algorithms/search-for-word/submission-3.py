class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def checkWord(r, c, board, index):
            if not self.isValid(r, c, board) or index >= len(word) or board[r][c] == "#":
                return False

            val = board[r][c]

            if val == word[index] and index == len(word) - 1:
                return True

            if val == word[index]:
                board[r][c] = "#" 
            
                found = (checkWord(r + 1, c, board, index + 1) or
                    checkWord(r - 1, c, board, index + 1) or
                    checkWord(r, c + 1, board, index + 1) or
                    checkWord(r, c - 1, board, index + 1))

                board[r][c] = val
                return found

            return False
            
            
        for r in range(len(board)):
            for c in range(len(board[r])):
                if checkWord(r, c, board, 0):
                    return True

        return False


    def isValid(self, r, c, board):
        return r >= 0 and r < len(board) and c >= 0 and c < len(board[r])
