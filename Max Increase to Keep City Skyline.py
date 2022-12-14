class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxRowVal = [0] * n
        maxColVal = [0] * n
        res = 0
        

        for i in range(n):
            for j in range(n):
                maxRowVal[i] = max(maxRowVal[i],grid[i][j])
                maxColVal[j] = max(maxColVal[j],grid[i][j])

        for i in range(n):
            for j in range(n):
                res = res + min(maxRowVal[i],maxColVal[j]) - grid[i][j]
        return res
