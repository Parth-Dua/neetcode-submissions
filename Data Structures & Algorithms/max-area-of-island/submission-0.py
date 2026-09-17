class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # Size of island
        def dfs_size_of_island(i,j): 

            if i<0 or i>= n or j<0 or j >=m or (i,j) in visited or grid[i][j] == 0: 
                return 0 
            
            # We know that this is 1 

            # Add to visited
            visited.add((i,j))

            # Recursive calls
            return 1 + dfs_size_of_island(i+1,j) + dfs_size_of_island(i,j+1) + dfs_size_of_island(i-1,j) + dfs_size_of_island(i,j-1)
   

        n, m = len(grid), len(grid[0])

        visited = set()
        max_area = 0 

        for i in range(n): 
            for j in range(m): 
                
                if grid[i][j] == 1 and (i,j) not in visited: 
                    size_of_this_island = dfs_size_of_island(i,j)
                    max_area = max(max_area, size_of_this_island) 

        return max_area
