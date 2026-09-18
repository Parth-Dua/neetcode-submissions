from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m= len(grid), len(grid[0])
        fresh_count = 0
        rotten_count = 0
        mins = 0
        # Count total fresh
        for i in range(n): 
            for j in range(m): 
                if grid[i][j] ==1: 
                    fresh_count += 1

                elif grid[i][j] == 2: 
                    rotten_count+=1
    
        if fresh_count != 0 and rotten_count == 0: 
            return -1
        if fresh_count == 0 and rotten_count == 0: 
            return 0

        
        # Start BFS with all rotten (2)
        queue = deque()

        for i in range(n): 
            for j in range(m): 
                if grid[i][j] == 2 : 
                    queue.append((i,j))


        while queue : 

            if fresh_count == 0 :
                return mins

            level_size = len(queue)

            for _ in range(level_size): 

                i,j = queue.popleft()

                neighbors = [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1)
                ]

                for x,y in neighbors: 

                    # 1. Bounds Check
                    if x<0 or x>=n or y<0 or y>=m: 
                        continue

                    # 2. WORK

                    if grid[x][y] == 1: 
                        # Change the fresh to rotten
                        grid[x][y] = 2
                        # Reduce the fresh count
                        fresh_count -= 1

                        # 3. Populate the queue
                        queue.append((x,y))

            mins+=1

        return -1


 
        