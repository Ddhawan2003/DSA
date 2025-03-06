class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        temp = image[sr][sc]
        if temp == color:
            return image
        def dfs(r,c):
            if r < 0 or r>=rows or c >=cols or c < 0 or temp!=image[r][c]:
                return
            image[r][c] = color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image
        