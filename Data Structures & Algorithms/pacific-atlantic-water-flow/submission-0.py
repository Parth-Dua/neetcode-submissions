class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # start with pacific - see what can reach pacific
        # start with atlantic to see what can reach atlantic at the same time 

        n,m = len(heights), len(heights[0])

        def bfs(queue, set_for_valid ): 
            
            while queue: 

                i,j = queue.popleft()

                neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

                for x,y in neighbors: 

                    if x<0 or x>=n or y<0 or y>=m or (x,y) in set_for_valid or heights[x][y] < heights[i][j]:
                        continue

                    # We know that this is a valid cell 
                    set_for_valid.add((x,y))
                    
                    # Add to the queue
                    queue.append((x,y))


        # FOR PACIFIC
        pacific_set = set()
        queue = deque()

        for i in range(n): 
            pacific_set.add((i,0))
            queue.append((i,0))

        for j in range(m): 
            pacific_set.add((0,j))
            queue.append((0,j))
        
        bfs(queue, pacific_set)
        
        
       # FOR ATLANTIC
        atlantic_set = set()
        queue = deque()

        for i in range(n): 
            atlantic_set.add((i,m-1))
            queue.append((i,m-1))

        for j in range(m): 
            atlantic_set.add((n-1,j))
            queue.append((n-1,j))
        
        bfs(queue, atlantic_set)

        # Return intersection of both sets 

        return list(pacific_set & atlantic_set)




