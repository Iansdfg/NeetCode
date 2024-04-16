from collections import deque
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    ROWS = 0
    COLS = 0
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        if not self.ROWS or not self.COLS:
            return 0
        island_no = 0
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if grid[row][col] == '1':
                    self.bfs(grid, row, col)
                    print(row, col)
                    island_no += 1
        return island_no

    def bfs(self, grid, row, col):
        queue = deque([(row, col)])
        grid[row][col] = '0'
        while queue:
            curr_row, curr_col = queue.popleft()
            for delta_row, delta_col in DIR:
                next_row, next_col = curr_row + delta_row, curr_col + delta_col
                if self.is_valid(grid, next_row, next_col):
                    grid[next_row][next_col] = '0'
                    queue.append((next_row, next_col))

    def is_valid(self, grid, row, col):
        if row < 0 or row >= self.ROWS:
            return False 
        if col < 0 or col >= self.COLS:
            return False 
        return grid[row][col] == '1'



        
