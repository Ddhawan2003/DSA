class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # islands = 0
        # rows = len(grid)
        # cols = len(grid[0])

        # def dfs(r,c):
        #     if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
        #         return
        #     grid[r][c] = "0"
        #     dfs(r-1,c)
        #     dfs(r+1,c)
        #     dfs(r,c-1)
        #     dfs(r,c+1)
        
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == "1":
        #             dfs(i,j)
        #             islands+=1
        # return islands

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            grid[r][c] == "0"

            while queue:
                row,col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1"):
                        grid[nr][nc] = '0'
                        queue.append((nr,nc))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands+=1
                    bfs(i,j)
        return islands

        

        