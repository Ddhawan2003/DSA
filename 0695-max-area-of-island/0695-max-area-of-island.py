class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            nonlocal area
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0
            area+=1
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j)
                    max_area = max(max_area, area)
                    
        return max_area
        