from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # Reverse order of BFS
        n = len(grid)
        m = len(grid[0])


        queue = deque()

        #Start BFS from all the treasure 

        for i in range(n): 
            for j in range(m): 
                if grid[i][j] == 0: 
                    queue.append((i,j))

        while queue: 
            i,j = queue.popleft()

            neighbors = [
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1)
            ]

            for x,y in neighbors: 

                # 1. Bounds check
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue

                # 2. WORK: 

                #Inelegible walls - 0, -1, already visited (NOT INF)
                if grid[x][y] != 2147483647: 
                    continue

                # For INF, increase the distance
                grid[x][y] = grid[i][j] + 1 

                
                # 3. Append the the queue
                queue.append((x,y))




        