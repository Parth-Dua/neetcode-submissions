class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        def dfs(i,j): 
            nonlocal visited
            if i < 0 or i > n-1 or j < 0 or j > m-1: 
                return
            if (i,j) in visited: 
                return 
            if grid[i][j] == '1': 
                visited.add((i,j))
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)

            else: 
                return
            

        # DFS as soon as you find a 
        n = len(grid)
        m = len(grid[0])

        visited = set()
        count = 0 
        for i in range(n): 
            for j in range(m): 

                if grid[i][j] == '1' and (i,j) not in visited: 
                    count+=1 
                    # Run DFS 
                    dfs(i,j)

        return count


