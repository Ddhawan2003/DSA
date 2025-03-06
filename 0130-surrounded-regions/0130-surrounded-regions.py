class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # Step 1: Mark all 'O's connected to borders as 'T'
        for i in range(rows):
            if board[i][0] == 'O':  # Left border
                dfs(i, 0)
            if board[i][cols - 1] == 'O':  # Right border
                dfs(i, cols - 1)

        for j in range(cols):
            if board[0][j] == 'O':  # Top border
                dfs(0, j)
            if board[rows - 1][j] == 'O':  # Bottom border
                dfs(rows - 1, j)

        # Step 2: Flip all remaining 'O's to 'X', and revert 'T' to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # ✅ Flip surrounded 'O' to 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'  # ✅ Restore border-connected 'O'
            

        