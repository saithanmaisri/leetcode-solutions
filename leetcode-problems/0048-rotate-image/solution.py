class Solution(object): 
    def rotate(self, matrix): 
        """ 
        :type matrix: List[List[int]] 
        :rtype: None Do not return anything, modify matrix in-place instead. 
        """ 
        cols = len(matrix[0]) 
        rows = len(matrix) 
        # Diagonal flip 
        for i in range(1, cols): 
            for j in range(i, cols): 
                row = i - 1 
                col = j 
                tmp = matrix[row][col] 
                matrix[row][col] = matrix[col][row] 
                matrix[col][row] = tmp 
        # Horizontal flip 
        l = 0 
        r = cols - 1 
        while l < r: 
            for i in range(0, rows): 
                tmp = matrix[i][l] 
                matrix[i][l] = matrix[i][r] 
                matrix[i][r] = tmp 
            l += 1 
            r -= 1
        return matrix
