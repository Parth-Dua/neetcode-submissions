class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ''' 


        '''
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) >1: 

            largest = heapq.heappop_max(heap)
            second_largest = heapq.heappop_max(heap)

            if largest != second_largest: 
                heapq.heappush_max(heap, largest-second_largest)

        
        if len(heap) == 0: 
            return 0

        return heap[0]