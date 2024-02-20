DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = self.bfs(grid, row, col)
                    max_area = max(area, max_area)
        return max_area

    def bfs(self, grid, x, y):
        area = 0
        queue = deque([(x, y)])
        grid[x][y] = 0
        while queue:
            curr_x, curr_y = queue.popleft()
            area += 1
            for delta_x, delta_y in DIRECTION:
                next_x, next_y = delta_x + curr_x, delta_y + curr_y
                if self.is_valid(grid, next_x, next_y):
                    grid[next_x][next_y] = 0
                    queue.append((next_x, next_y))

        return area
    
    def is_valid(self, grid, x, y):
        rows = len(grid)
        cols = len(grid[0])

        if x < 0 or x >= rows:
            return False 
        if y < 0 or y >= cols:
            return False 
        return grid[x][y] == 1 


        
