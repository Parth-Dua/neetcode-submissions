class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # Multi source BFS - start with the chests 
        n, m = len(grid), len(grid[0])

        queue = deque()

        for i in range(n): 
            for j in range(m): 
                if grid[i][j] == 0: 
                    queue.append((i,j))

        
        while queue: 

            i,j = queue.popleft()

            neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1) ]

            for x,y in neighbors: 

                if x<0 or x>=n or y<0 or y>=m or grid[x][y] != 2147483647: 
                    continue

                # Now the neighbors are valid and the ones that are not already visited 

                grid[x][y] = grid[i][j] + 1 

                # Add to queue
                queue.append((x,y))


        
