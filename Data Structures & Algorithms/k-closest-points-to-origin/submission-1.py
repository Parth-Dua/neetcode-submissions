class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        map_dist_to_points = defaultdict(list) # dist -> [[2,3], [3,2]]

        distances = []

        for i in range(len(points)): 
            dist = (points[i][0] )**2 + (points[i][1] ) **2
            map_dist_to_points[dist].append(points[i])
            distances.append(dist)

        ans = []
        # Min Heap
        heapq.heapify(distances) # O( n)


        for _ in range(k): 

            dist = heapq.heappop(distances)
            ans.append(map_dist_to_points[dist].pop())

        return ans


