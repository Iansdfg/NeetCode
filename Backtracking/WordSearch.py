DIRCTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
class Solution:
    res = False 
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for i in range(cols)] for j in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    visited[row][col] = 1
                    self.dfs(board, word, word[0], 1, row, col, rows, cols, visited)
                    visited[row][col] =0

        return self.res 

    def dfs(self, board, target, curr_word, index, curr_row, curr_col, rows, cols, visited):
        if index > len(target):
            return  

        if target == curr_word:
            self.res = True 
            return 
    
        for delta_row, delta_col in DIRCTIONS:
            next_row = curr_row + delta_row
            next_col = curr_col + delta_col
            if not self.is_valid(board, target, index, curr_word, next_row, next_col, rows, cols, visited):
                continue 

            visited[next_row][next_col] = 1
            curr_word += board[next_row][next_col]
            res = self.dfs(board, target, curr_word, index + 1, next_row, next_col, rows, cols, visited)
            curr_word = curr_word[:-1]
            visited[next_row][next_col] = 0


    def is_valid(self, board, target, index, curr_word, row, col, rows, cols, visited):
        if row < 0 or row >= rows:
            return False 
        if col < 0 or col >= cols:
            return False
        if board[row][col] != target[index]:
            return False 
        return visited[row][col] == 0 


