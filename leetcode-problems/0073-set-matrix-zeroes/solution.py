class Solution(object): 
    def setZeroes(self, matrix): 
        """ 
        :type matrix: List[List[int]] 
        :rtype: None Do not return anything, modify matrix in-place instead. 
        """ 
        m, n = len(matrix), len(matrix[0]) 
        zeros = [0] * (m + n) # Array to store rows and columns with zeros 
        # Mark the rows and columns to be zeroed 
        for i in range(m): 
            for j in range(n): 
                if matrix[i][j] == 0: 
                    zeros[i] = 1 
                    zeros[m + j] = 1 
        # Update the matrix based on the zeros array 
        for i in range(m): 
            for j in range(n): 
                if zeros[i] == 1 or zeros[m + j] == 1: 
                    matrix[i][j] = 0
