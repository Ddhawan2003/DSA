class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c, i):
            if i == len(word):
                return True
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] != word[i]:
                return False
            temp = board[r][c]
            board[r][c] = "#"
            res = (dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1))
            board[r][c] = temp
            return res

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j, 0):
                        return True
        return False
        