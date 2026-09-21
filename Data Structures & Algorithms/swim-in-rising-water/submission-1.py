class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # Greedy + heap 

        minheap = [(grid[0][0], 0,0)]
        n = len(grid)
        visited = set()

        ans = 0

        while (n-1,n-1) not in visited: 
            cost, i,j   = heapq.heappop(minheap)
            # NO need if already visited 
            if (i,j) in visited: 
                continue

            visited.add((i,j))
            ans = max(ans, cost)

            for x, y in [(i-1,j), (i+1,j), (i,j+1), (i,j-1)]: 

                if 0 <= x < n and 0 <= y < n and (x,y) not in visited: 
                    heapq.heappush(minheap, (grid[x][y], x, y))


        return ans 
