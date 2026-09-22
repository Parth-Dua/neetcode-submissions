class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # PRIM - MST 

        minheap = [(0,points[0][0], points[0][1])] # (dist, x,y)

        visited = set()
        min_dist = 0

        while minheap: 
            dist, i, j = heapq.heappop(minheap)

            if (i,j) in visited: 
                continue
            
            # unvisited one with the min distance - greedy approach - finalize this
            visited.add((i,j))
            min_dist += dist 
            
            for x,y in points: 

                if (x,y) not in visited:
                    d_bw_points = abs(x-i) + abs(y-j)
                    heapq.heappush(minheap, (d_bw_points, x, y ))

        return min_dist
                    


