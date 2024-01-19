DIRCTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution(object):
    found = False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    visited.add((row, col))
                    self.dfs(row, col, board, word[1:], visited)
                    visited.remove((row, col))
        return self.found

    def dfs(self, row, col, board, word, visited):
        if len(word) == 0:
            self.found = True
            return 
        

        for row_delta, col_delta in DIRCTION:
            new_row, new_col = row + row_delta, col + col_delta

            if not self.is_valid(new_row, new_col, board, word, visited):
                continue

            visited.add((new_row, new_col))
            self.dfs(new_row, new_col, board, word[1:], visited)
            visited.remove((new_row, new_col))
        
        return 


    def is_valid(self, row, col, board, word, visited):
        if (row, col) in visited:
            return False 
        if col < 0 or col >= len(board[0]):
            return False 
        if row < 0 or row >= len(board):
            return False
        return board[row][col] == word[0] 
