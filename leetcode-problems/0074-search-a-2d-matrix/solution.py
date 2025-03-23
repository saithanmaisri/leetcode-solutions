class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if row and row[-1] >= target:  # Added check for empty rows
                if target in row:
                    return True
                else:
                    return False
        return False
