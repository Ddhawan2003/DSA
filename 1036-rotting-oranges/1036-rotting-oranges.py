class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh = 0
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # ⬇️ Move this outside the loop
        if fresh == 0:
            return 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            time += 1

        return time if fresh == 0 else -1