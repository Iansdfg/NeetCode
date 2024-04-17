from collections import deque
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    rows = 0
    cols = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        max_area = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    area = self.bfs(grid, row, col)
                    max_area = max(max_area, area)
        return max_area

    def bfs(self, grid, row, col):
        queue = deque([(row, col)])
        grid[row][col] = 0
        area = 1

        while queue: 
            curr_row, curr_col = queue.popleft()
            for delta_row, delta_col in DIR:
                next_row = delta_row + curr_row
                next_col = delta_col + curr_col
                if self.is_valid(grid, next_row, next_col):
                    queue.append((next_row, next_col))
                    area += 1 
                    grid[next_row][next_col] = 0
        return area

    def is_valid(self, grid, row, col):
        if row < 0 or row >= self.rows:
            return False 
        if col < 0 or col >= self.cols:
            return False 
        return grid[row][col] == 1 
        
