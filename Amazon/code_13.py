class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rotting(rotten):
            temp = []
            for i, j in rotten:
                # top
                if i > 0 and grid[i - 1][j] == 1:
                    temp.append((i-1,j))
                    grid[i-1][j] = 2
                #bottom
                if i < rows - 1 and grid[i + 1][j] == 1:
                    temp.append((i+1,j))
                    grid[i+1][j] = 2
                # left
                if j > 0 and grid[i][j - 1] == 1:
                    temp.append((i,j-1))
                    grid[i][j-1] = 2
                # right
                if j < cols - 1 and grid[i][j + 1] == 1:
                    temp.append((i,j+1))
                    grid[i][j + 1] = 2
            return temp
        
        rows = len(grid)
        cols = len(grid[0])
        
        rotten = [(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 2]
        
        count = 0
        
        while rotten:
            rotten = rotting(rotten)
            if len(rotten) == 0:
                break
            count += 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                
        return count