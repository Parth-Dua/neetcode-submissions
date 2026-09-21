class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
    
        island_area = 0

        def dfs(i,j): 
            nonlocal island_area
            if i<0 or i>=n or j<0 or j>=m: 
                return  

            if grid[i][j] == 0:
                return

            # Found a 1
            island_area +=1 
            grid[i][j] = 0 # Mark as visited

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

            return

        max_area = 0
        for i in range(n): 
            for j in range(m): 
                dfs(i,j)
                max_area = max(max_area, island_area) 
                island_area = 0

        return max_area 