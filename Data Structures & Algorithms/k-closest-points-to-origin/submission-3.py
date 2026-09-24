class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        '''
        distances = [4,2,9,10,1]
        maxheap -> remove the largest n-k elements -> remaining k smallest elements
        '''

        distances = []

        for x,y in points: 
            dist = x**2 + y**2
            distances.append((dist, x, y))

        heapq.heapify_max(distances) # O(n)
        n = len(distances)

        for _ in range(n-k):  
            heapq.heappop_max(distances) # O(log n)

        # O(n+ (n-k)(log n))
        return [[x,y] for d,x,y in distances]
