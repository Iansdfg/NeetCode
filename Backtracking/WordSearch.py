DIRCTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution(object):
    found = False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for i in range(cols)] for j in range(rows)]  #op1 use matrx instead of set

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    visited[row][col] = 1
                    self.dfs(row, col, board, word[1:], visited)
                    visited[row][col] = 0
        return self.found

    def dfs(self, row, col, board, word, visited):
        if len(word) == 0:
            self.found = True
            return 
        
        for row_delta, col_delta in DIRCTION:
            new_row, new_col = row + row_delta, col + col_delta

            if not self.is_valid(new_row, new_col, board, word, visited):
                continue

            visited[row][col] = 1
            self.dfs(new_row, new_col, board, word[1:], visited)
            visited[row][col] = 0
        
    def is_valid(self, row, col, board, word, visited):
        if col < 0 or col >= len(board[0]):
            return False 
        if row < 0 or row >= len(board):
            return False
        if visited[row][col] == 1:
            return False 
        return board[row][col] == word[0] 
