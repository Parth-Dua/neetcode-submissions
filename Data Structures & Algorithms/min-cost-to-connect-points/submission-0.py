class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # Prim

        minheap = [(0, points[0][0],points[0][1])]

        visited = set()

        final_cost = 0 

        while len(visited) != len(points): 

            cost, i,j = heapq.heappop(minheap) # ONE WITH MIN VAL - greedy 

            if (i,j) in visited: 
                continue 

            final_cost+=cost 
            
            # HAVE TO FIND THE DISTANCE WITH ALL THE POINTS NOT visited
            visited.add((i,j))

            for x,y in points: 
                if (x,y) not in visited: 
                    dist = abs(i-x) + abs(j-y)
                    heapq.heappush(minheap, (dist, x, y))

        return final_cost 


