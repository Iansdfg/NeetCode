class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_res = self.check_rows(board)
        col_res = self.check_cols(board)
        sq_res = self.check_sq(board)
        return row_res and col_res and sq_res

    def check_cols(self, board):
        for col in range(9):
            used = set()
            for row in range(9):
                if not self.check_valid(board[col][row], used):
                    return False
        return True 
                
    def check_rows(self, board):
        for col in range(9):
            used = set()
            for row in range(9):
                if not self.check_valid(board[row][col], used):
                    return False
        return True 

    def check_sq(self, board):
        for i in range(3):
            for j in range(3):
                used = set()
                for row in range(i*3, i*3 + 3):
                    for col in range(j*3, j*3 + 3):
                        if not self.check_valid(board[row][col], used):
                            return False
        return True 

    def check_valid(self, c, used):
        if c == '.':
            return True 
        if c in used:
            return False 
        used.add(c)
        return True
        

        
