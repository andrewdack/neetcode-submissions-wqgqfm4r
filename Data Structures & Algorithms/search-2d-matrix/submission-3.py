class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lR, rR = 0, len(matrix) - 1
        mR = (lR + rR) // 2

        print(mR)
        # row binary search
        tRow = -1
        while lR <= rR:
            if matrix[mR][0] == target:
                return True
            elif matrix[mR][0] > target:
                rR = mR - 1
                tRow = rR
            elif matrix[mR][0] < target:
                lR = mR + 1
                if matrix[mR][-1] >= target:
                    tRow = lR - 1
                else:
                    tRow = lR
            
            mR = (lR + rR) // 2

        print(tRow)
        if tRow >= len(matrix):
            return False
        # column binary search
        l, r = 0, len(matrix[tRow]) - 1
        print(l, r)
        m = (l + r) // 2
        while l <= r:
            if (matrix[tRow][m] == target):
                return True
            elif matrix[tRow][m] > target:
                r = m - 1
            elif matrix[tRow][m] < target:
                l = m + 1
            
            m = (l + r) // 2
        print(m)
        return False