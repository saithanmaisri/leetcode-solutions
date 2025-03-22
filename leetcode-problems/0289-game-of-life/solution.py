class Solution(object): 
    def gameOfLife(self, board): 
        new = [row[::] for row in board] 
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)] 
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                c_live = 0 
                for d in directions: 
                    x = i+d[0] 
                    y = j+d[1] 
                    if 0<=x<len(board) and 0<= y< len(board[0]) and new[x][y]: 
                        c_live +=1 
                if new[i][j]: 
                    if c_live !=2 and c_live !=3: 
                        board[i][j]=0 
                else: 
                    if c_live ==3: 
                        board[i][j]=1
