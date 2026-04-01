class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lR, rR = 0, len(matrix) - 1
        mR = (lR + rR) // 2

        # row binary search
        tRow = -1
        while lR <= rR:
            if matrix[mR][0] == target:
                return True
            elif target > matrix[mR][-1]:
                lR = mR + 1
                tRow = lR
            elif target < matrix[mR][0]:
                rR = mR - 1
                tRow = rR
            else:
                tRow = mR
                break;
            
            mR = (lR + rR) // 2

        if tRow >= len(matrix):
            return False
        # column binary search
        l, r = 0, len(matrix[tRow]) - 1
        m = (l + r) // 2
        while l <= r:
            if (matrix[tRow][m] == target):
                return True
            elif matrix[tRow][m] > target:
                r = m - 1
            elif matrix[tRow][m] < target:
                l = m + 1
            
            m = (l + r) // 2
        return False