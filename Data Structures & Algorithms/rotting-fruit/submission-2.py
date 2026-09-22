class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Levels required to counter all the oranges 

        # Brute force = BFS from all the fresh till they reach the nearest rotten

        queue = deque()

        n,m = len(grid), len(grid[0])

        count_1 = 0 

        for i in range(n): 
            for j in range(m) :
                if grid[i][j] == 1: 
                    count_1 +=1 
                if grid[i][j] == 2: 
                    queue.append((i,j))

        count_1_found = 0

        time = 0
        c = 0

        queue_size = len(queue)
        while queue: 
            
            if c == queue_size:  #All completed for this level 
                time+=1
                queue_size = len(queue)
                c = 0


            i,j = queue.popleft()

            neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

            for x,y in neighbors: 

                if x<0 or x>=n or y<0 or y>=m or grid[x][y]!= 1: 
                    continue 
                
                # We have a fresh fruit 
                count_1_found +=1 
                grid[x][y] = 2
                queue.append((x,y))

            c+=1

        if count_1_found!= count_1: 
            return -1

        return time 

        


